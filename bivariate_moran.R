library(scales)
library(stringr)
library(ape)

# Bivariate Moran's I
moran_I <- function(x, y = NULL, W){
  if(is.null(y)) y = x
  
  xp <- scale(x)[, 1]
  yp <- scale(y)[, 1]
  W[which(is.na(W))] <- 0
  n <- nrow(W)
  
  global <- (xp%*%W%*%yp)/(n - 1)
  local  <- (xp*W%*%yp)
  
  list(global = global, local  = as.numeric(local))
}


# Permutations for the Bivariate Moran's I
simula_moran <- function(x, y = NULL, W, nsims = 30000){
  if(is.null(y)) y = x
  
  n   = nrow(W)
  IDs = 1:n
  
  xp <- scale(x)[, 1]
  #xp <- (x - sapply(x, mean))/sapply(x, sd) #xp <- (x - mean(x, na.rm=T))/sd(x, na.rm=T)
  W[which(is.na(W))] <- 0
  
  global_sims = NULL
  local_sims  = matrix(NA, nrow = n, ncol=nsims)
  
  ID_sample = sample(IDs, size = n*nsims, replace = T)
  
  y_s = y[ID_sample,1]
  y_s = matrix(y_s, nrow = n, ncol = nsims)
  y_s <- (y_s - apply(y_s, 1, mean))/apply(y_s, 1, sd)
  
  global_sims  <- as.numeric( (xp%*%W%*%y_s)/(n - 1) )
  local_sims  <- (xp*W%*%y_s)
  
  list(global_sims = global_sims,
       local_sims  = local_sims)
 
}

W <- read.csv("transformed_data/1000x1000/macierz_sasiedztwa.csv",header = FALSE ,sep=";")
W  <- as.matrix(W/rowSums(W))
W[which(is.na(W))] <- 0
x <- read.csv("transformed_data/1000x1000/przypadki.csv",header = FALSE ,sep=";")
y <- read.csv("transformed_data/1000x1000/budynki.csv",header = FALSE ,sep=";")

print("Univariate Moran Index")
univariate_moran_global <- Moran.I(y$V1,W)
univariate_moran_global

m <- moran_I(x, y, W)

# Global Moral
global_moran <- m[[1]][1]
#> 0.2218409

# Local values
m_i <- m[[2]] 

# local simulations
local_sims <- simula_moran( x,y, W)$local_sims


# global pseudo p-value  
# get all simulated global moran
global_sims <- simula_moran( x,y, W)$global_sims

# Proportion of simulated global values taht are higher (in absolute terms) than the actual index 
moran_pvalue <- sum(abs(global_sims) > abs( global_moran )) / length(global_sims)
#> 0


# Identifying the significant values 
alpha <- .001  # for a 95% confidence interval
probs <- c(alpha/2, 1-alpha/2)
intervals <- t( apply(local_sims, 1, function(x) quantile(x, probs=probs)))
sig       <- ( m_i < intervals[,1] )  | ( m_i > intervals[,2] )

print(moran_pvalue)
print(global_moran)


#write.csv(m_i,'r_out/pruszkowski/1000x1000/budynki.csv')

# Preparing for plotting


# Identifying the LISA clusters
xp <- scale(x)[,1]
yp <- scale(y)[,1]


patterns <- as.character( interaction(xp > 0, W%*%yp > 0) )
patterns <- patterns %>% 
  str_replace_all("TRUE","High") %>% 
  str_replace_all("FALSE","Low")

patterns[sig==0] <- "Not significant"
patterns <- data.frame(patterns)
write.csv(patterns,'r_out/pruszkowski/1000x1000/hot-cold/budynki.csv',row.names = FALSE)




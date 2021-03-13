### ------------------------------------------------------------------------ ###
##                                 nohaze.R                                   ##
##          this is a code to analyse SMEAR-II in situ data in R              ##
##               developed for The Arctic Hackathon                           ##
##             event link: https://hackthearctic.com/                         ##
##             created by: Pramit Deb Burman, IITM Pune                       ##
##                   first created on: 13 March 2021                          ##
##                   revision history:                                        ##
### ------------------------------------------------------------------------ ###

### --------------------- START OF THE PROGRAM ----------------------------- ###

##  --------------------- set the working directory
setwd("")

#   --------------------- load required packages
library(urltools)
library(lubridate)

#   ------ read the date of interest
species <- 'NOx'    # choices are CO2, CO and NOx

#   ------ EDIT: need to put the drop-down menu here
#   ------ by default measurements at the level closest to the surface (i.e. 4.2 m here) are considered

#   --------------------- today's date
date1 <- Sys.Date()

#   --------------------- create one-month window
date2 <- date1 %m-% months(1)

#   -------------------- load data directly (from SMEAR II webpage)
inp1 <- read.csv('https://smear-backend.rahtiapp.fi/search/timeseries/csv?tablevariable=HYY_META.NOx42&from=2021-02-12T00%3A00%3A00.000&to=2021-03-12T23%3A59%3A59.999&quality=ANY&aggregation=ARITHMETIC&interval=30')

check <- paste('https://smear-backend.rahtiapp.fi/search/timeseries/csv?tablevariable=HYY_META.',species,'42&from=',date2,'T00%3A00%3A00.000&to=',date1,'T23%3A59%3A59.999&quality=ANY&aggregation=ARITHMETIC&interval=30',sep = "")

inp2 <- read.csv(check)

#  -------------------- plotting the data [EDIT BELOW SNIPPET]
png('vis1.png', width = 10, height = 8, units = "in", res = 600)
par(mar = c(10.8, 5, 10.8, 2), mfrow = c(1, 2))
plot(knr, main = "Kmeans", yaxt = 'n', col = viridis_pal(option = "D")(10))
dev.off()

### ---------------------- END OF THE PROGRAM ------------------------------ ###
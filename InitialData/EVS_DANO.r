### Arseny Verkeev for DANO 2021 ###
setwd("C:/Users/user/YandexDisk/R/evs_dano_2021")
library(dplyr); library(sjlabelled)

# EVS (2020). European Values Study 2017: Integrated Dataset (EVS 2017). 
# GESIS Data Archive, Cologne. 
# ZA7500 Data file Version 4.0.0, https://doi.org/10.4232/1.13560.
e <- haven::read_dta("ZA7500_v4-0-0.dta")

# Russian Federation, fieldwork: 07-11-2017 – 25-12-2017, mode: CAPI/PAPI, n=1825
e <- e %>% filter(e$c_abrv=="RU")


# show values of certain variables
# sex
summary(as.factor(e$v225))
summary(as.factor(as_label(e$v225)))

# age
summary(as.factor(e$age))
summary(as.factor(as_label(e$age)))

# status
summary(as.factor(e$v234))
summary(as.factor(as_label(e$v234)))

# income
summary(as.factor(e$v261_r))
summary(as.factor(as_label(e$v261_r)))

# satisfaction
summary(as.factor(e$v39))
summary(as.factor(as_label(e$v39)))

# believe in God
summary(as.factor(e$v57))
summary(as.factor(as_label(e$v57)))

# believe in hell
summary(as.factor(e$v59))
summary(as.factor(as_label(e$v59)))

# immigrants
summary(as.factor(e$v186))
summary(as.factor(as_label(e$v186)))


# select variables for DANO
e2 <- e %>% select(
    
    sex = v225, # sex respondent (Q63)
    age, # age: respondent (constructed) (Q64)
    status = v234, # current legal marital status respondent (Q72)
    income = v261_r, # household total net income (Q98) (income level)
    
    satisfaction = v39, # how satisfied are you with your life (Q10)
    trust = v35, # how much you trust: people you meet for the first time (Q8D)
    god = v57, # do you believe in: God (Q18A)
    hell = v59, # do you believe in: hell (Q18C)
    immigrants = v186, # immigrants increase crime problems (Q52B)
    
) %>% mutate(
    sex = case_when(sex==1~"male", sex==2~"female") # make sex categorical
)

# fix spelling of NA values
e2[e2 < 0] <- NA

# write the dataframe to csv file
write.csv(e2, "EVS_DANO_2021.csv", row.names = F)

# check if the prepared csv file reads well
df <- read.csv("EVS_DANO_2021.csv")

# drop objects from environment
rm(e, e2, df)

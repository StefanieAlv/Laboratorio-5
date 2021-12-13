#Variables categoricas con NA
CATEGORICAL_VARS_WITH_NA_FREQUENT = ['Embarked']

#Variable categoricas con NA pero indicador de Missing
CATEGORICAL_VARS_WITH_NA_MISSING = []


#Variables numéricas con NA
NUMERICAL_VARS_WITH_NA = ['Age']


#Variables de temporalidad
#TEMPORAL_VARS = ['']
#REF_VAR = ""

#Varaibles que vamos a tirar
DROP_FEATURES = []

#Varibles para transformación logarítmica
NUMERICALS_LOG_VARS = [] #"Fare"

#Variables para binarización por sesgo fuerte
BINARIZE_VARS = []

#Variables para hacer mapeo categorico por codificación ordinal
Lista_Sex = ['Sex']
Lista_E = ['Embarked']

#Variables categoricas a codificar sin ordinalidad
#CATEGORICAL_VARS = []

#Mapeos de variables categoricas
Diccio_Sex = {'female':1, 'male':2, '3':3, 'Missing':0, 'NA':0, 'NaN':0}
Diccio_E = {'C':1, 'Q':2, 'S':3, 'Missing':0, 'NA':0, 'NaN':0}

#Variables seleccionadas según análisis de Lasso
FEATURES = [
    'Pclass', 
    'Sex', 
    'Age', 
    'SibSp', 
    'Embarked',
]
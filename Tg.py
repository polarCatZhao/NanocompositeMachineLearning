import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#file = 'Tg.CSV'
file = 'tan_delta_study.CSV'

df = pd.read_csv(file)

df['folderID']=df['folderID'].astype(str)

print(df.info())

for i in range(len(df.index)):
    df.loc[i,'folderID'] = 'p'+ df.loc[i,'folderID']


base_dict = dict()
for index, row in df.iterrows():
    if row['filler percentage']==0:
        base_dict[row['folderID']] = row['Tg']

df['normalized_Tg'] = df.apply(lambda row: row['Tg'] - base_dict[row['folderID']], axis = 1)

folderID_list = list()
coef_list = list()
intercept_list = list()
R_squared_list = list()
rmse_list = list()
matrix_list = list()
filler_list = list()
for id in df.folderID.unique():
    df_each_paper = df[df['folderID']==id]
    y = df_each_paper['normalized_Tg'].values
    X = df_each_paper['filler percentage'].values
    y = y.reshape(-1, 1)
    X = X.reshape(-1, 1)

    reg = LinearRegression()
    prediction_space = np.linspace(min(X), max(X)).reshape(-1, 1)

    reg.fit(X, y)
    y_pred = reg.predict(X)
    y_pred2 = reg.predict(prediction_space)

    #print(id)
    #print("R^2: ", reg.score(X, y))
    #print("coef: ", reg.coef_)
    #print('intercept:', reg.intercept_)
    folderID_list.append(id)
    coef_list.append(reg.coef_[0][0])
    intercept_list.append(reg.intercept_[0])
    R_squared_list.append(reg.score(X, y))
    rmse_list.append(np.sqrt(mean_squared_error(y, y_pred)))
    matrix_list.append(df_each_paper.iloc[0, 1])
    filler_list.append(df_each_paper.iloc[0, 2])
    #print(df_each_paper.iloc[0, 1])

    if id == 'p14':
        print(reg.score(X, y))
        plt.figure()
        sns.scatterplot(x = 'filler percentage', y = 'normalized_Tg', data = df_each_paper, hue ='folderID')
        plt.plot(prediction_space, y_pred2, color ='black', linewidth = 3)
        plt.show()

list_values = [folderID_list, coef_list, intercept_list, R_squared_list, rmse_list, matrix_list, filler_list]
list_keys = ['folderID', 'coef', 'intercept', 'R_squared', 'RMSE','matrix', 'filler']
zipped = list(zip(list_keys, list_values))
data = dict(zipped)
df_results = pd.DataFrame(data)
df_results_rmse_sorted = df_results.sort_values('RMSE')
#df_results_rmse_sorted.to_csv('results_rmse_sorted.csv')
#df_results_sorted = df_results.sort_values('coef')
#df_results_sorted.to_csv('results_sorted.csv')
#df_results.to_csv('results_3.csv')
#df_results.to_csv('results_2.csv')
print('coef mean, median, std, min, max, 75%: ', np.mean(coef_list),'    ', np.median(coef_list),'   ', np.std(coef_list),'  ', np.amin(coef_list),' ' ,np.amax(coef_list),'    ',np.percentile(coef_list, 75))
print('R_squared mean, median, std, min, max, 75%: ', np.mean(R_squared_list),'  ' ,np.median(R_squared_list), ' ',np.std(R_squared_list),'  ', np.amin(R_squared_list),'    ' ,
      np.amax(R_squared_list),'   ', np.percentile(R_squared_list, 75))
print('rmse mean, median, std, min, max, 75%: ', np.mean(rmse_list),'  ' ,np.median(rmse_list), ' ',np.std(rmse_list),
      '  ', np.amin(rmse_list),'    ' ,np.amax(rmse_list),' ', np.percentile(rmse_list, 75))

#figures of sorted (by rmse) results
'''
plt.figure()
plt.title('sorted rmse')
sns.scatterplot(x='folderID', y='RMSE', data= df_results_rmse_sorted, hue='filler',legend='full')
plt.legend(bbox_to_anchor=(0.97, 0), loc = 3)
plt.show()
'''
'''
#figures of sorted (by coef) results
plt.figure()
plt.title('sorted coefficent')
sns.scatterplot(x ='folderID', y='coef',data= df_results_sorted, hue = 'RMSE', legend= 'full')
plt.legend(bbox_to_anchor=(0.97, -0.2), loc = 3)
plt.show()
'''
'''
# figures for results
plt.figure()
plt.title('coefficient')
sns.scatterplot(folderID_list, coef_list, hue= matrix_list, legend='full')
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.legend(bbox_to_anchor=(0.97, -0.1), loc = 3, borderaxespad = 0.)
plt.show()

plt.figure()
plt.title('coefficient')
sns.scatterplot(folderID_list, coef_list, hue= filler_list, legend='full')
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.legend(bbox_to_anchor=(0.97, -0.1), loc = 3, borderaxespad = 0.)
plt.show()

plt.figure()
plt.title('R_squrared')
sns.scatterplot(folderID_list, R_squared_list, hue= filler_list)
plt.legend(bbox_to_anchor=(0.97, -0.1), loc = 3, borderaxespad = 0.)
plt.show()

plt.figure()
plt.title('RMSE')
sns.scatterplot(folderID_list, rmse_list, hue= filler_list)
plt.legend(bbox_to_anchor=(0.97, -0.1), loc = 3, borderaxespad = 0.)
plt.show()
'''

'''
print(base_dict)

for id in df.folderID.unique():
    if id not in base_dict.keys():
        print(id + 'does not have base line')
'''
"""
#raw data figure
plt.figure()
plot = sns.scatterplot(x='filler percentage', y='normalized_Tg',hue='filler', size='filler', data=df, legend='full')
plt.legend(bbox_to_anchor=(0.97, -0.15), loc =3)
#plt.setp(plot.get_legend().get_texts(), fontsize = '9')
plt.show()
"""
'''
plt.figure()
g = sns.FacetGrid(df, col="folderID",col_wrap=10, height =2.5)
g.map(plt.scatter, "filler percentage", "new_Tg")
plt.show()
'''
'''
#df.take(list(range(150)))
plt.figure()
g = sns.FacetGrid(df.take(list(range(100))), col="folderID",col_wrap=5, height =3, aspect= 3)
g.map(plt.scatter, "filler percentage", "new_Tg")
plt.show()
'''
'''
for id in df.folderID.unique():
    #print(id)
    #print(df[df['folderID']==id])
    plt.figure()
    sns.scatterplot(x ='filler percentage', y='new_Tg', data=df[df['folderID'] == id], hue='folderID')
    plt.show()
'''






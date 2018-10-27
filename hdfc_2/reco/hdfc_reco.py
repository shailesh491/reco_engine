from scipy import spatial
import pandas as pd

def get_recommendation(selection):
    list_name =[]
    list_sim =[]
    final_names = []
    metadata = pd.read_csv('hdfd_property_data_csv1.csv')
    for i in range(len(metadata)):
        result = 1 - spatial.distance.cosine(metadata.iloc[selection,2:], metadata.iloc[i,2:])
        list_name.append(metadata.iloc[i,1])
        list_sim.append(result)
    list1 = sorted(list_sim)

    for i in range(len(list_sim)):
        if (list1[-2] == list_sim[i]):
            final_names.append(list_name[i])
        
    for i in range(len(list_sim)):
        if (list1[-3] == list_sim[i]):
            final_names.append(list_name[i])
        
    for i in range(len(list_sim)):
        if (list1[-4] == list_sim[i]):
            final_names.append(list_name[i])

    for i in range(len(list_sim)):
        if (list1[-5] == list_sim[i]):
            final_names.append(list_name[i])
        
    for i in range(len(list_sim)):
        if (list1[-6] == list_sim[i]):
            final_names.append(list_name[i])
    return (final_names)

print(get_recommendation(67))


import pandas as pd

df_demo = pd.read_csv('raw/df_final_demo.csv')
df_wd1 = pd.read_csv('raw/df_final_web_data_pt_1.csv')
df_wd2 = pd.read_csv('raw/df_final_web_data_pt_2.csv')
df_exp = pd.read_csv('raw/df_final_experiment_clients.csv')  

web = pd.concat([df_wd1, df_wd2], ignore_index=True) # Combine the two web data files into one dataframe.

def process_step_counts():
    step_counts = web['process_step'].value_counts().reset_index()
    step_counts.columns = ['process_step', 'count']
    return step_counts



def age_group(clnt_age):
    if clnt_age >= 16 and clnt_age <= 30:
        return 'Younger'
    elif 30 < clnt_age <= 50:
        return 'Adult'
    elif 50 < clnt_age <= 70:
        return 'Senior'
    else:
        return 'Oldie'
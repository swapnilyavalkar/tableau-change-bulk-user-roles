from datetime import datetime
import pandas as pd
import tableauserverclient as TSC
import config

# Creator
# Explorer
# ExplorerCanPublish
# Unlicensed
# Viewer

df_restored_access = pd.DataFrame(columns=['site_name', 'user_name', 'previous_role', 'new_role'])

if __name__ == '__main__':
    print("Connecting to Tableau Server: " + config.server)
    now = datetime.now()
    date_to_be_used = now.strftime("%d-%m-%Y %H-%M-%S")
    df = pd.read_csv('users_roles_update.csv')
    for index, df_row in df.iterrows():
        tableau_auth = TSC.TableauAuth(config.user_name, config.password, site_id=df_row['site'])
        server = TSC.Server(config.server)
        server.add_http_options({'verify': False})
        server.use_server_version()
        req_option = TSC.RequestOptions()
        req_option.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name,
                                         TSC.RequestOptions.Operator.Equals,
                                         df_row['username']))
        with server.auth.sign_in(tableau_auth):
            user_item, pagination = server.users.get(req_option)
            if user_item[0].name == df_row['username'] and user_item[0].site_role != df_row['role']:
                previous_role = user_item[0].site_role
                user_item[0].site_role = df_row['role']
                user = server.users.update(user_item[0])
                df_restored_access = df_restored_access.append({'site_name': df_row['site'],
                                                                 'user_name': user.name,
                                                                'previous_role': previous_role,
                                                                'new_role': user.site_role},
                                                               ignore_index=True)
                print(user.name + ' role changed to: ' + user.site_role)
            else:
                df_restored_access = df_restored_access.append({'site_name': df_row['site'],
                                                                'user_name': df_row['username'],
                                                                'previous_role': df_row['role'],
                                                                'new_role': "NOT REQUIRED"},
                                                               ignore_index=True)
                print(df_row['username'] + ' role not changed to: ' + df_row['role'])
print(df_restored_access.to_string())
filename = date_to_be_used + "-Restored Access.xlsx"
df_restored_access.to_excel("data-files\\" + filename, sheet_name="Updated Users Roles", index=False)
print("All Users Are Updated !!!")

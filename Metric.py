import pandas as pd

class Metric:
    def __init__(self, metric, hr, field_name):
        self.df = None
        self.metric = metric
        self.hr_team = hr.get_id_team_data()
        self.hr_size = hr.get_number_of_people_team()

        self.field_name = field_name

    def load_data(self):
        self.df = pd.read_csv('data/{}.csv'.format(self.metric))
        
    def merge_with_team(self):
        self.df = self.df.merge(self.hr_team[['Team', 'Employee_ID']], how='left', left_on=['Employee_ID'],
                                right_on=['Employee_ID'])

    def group_and_count(self):
        pass

    def zero_data_handling(self):
        self.df = self.hr_size[['Team']]
        self.df[self.field_name] = 0

    def get_df(self):
        self.load_data()
        if len(self.df) != 0:
            self.merge_with_team()
            self.group_and_count()
            if len(self.df) == 0: # there are times where the metric is available but not for this team
                self.zero_data_handling()
        else:
            self.zero_data_handling()
        self.df = self.df.drop_duplicates(subset=['Team'])
        return self.df

class Overtime(Metric):
    def __init__(self, hr):
        super().__init__('Overtime', hr,  'Overtime per employee')
    
    def group_and_count(self):
        self.df = self.df.groupby('Team')['Overtime_Hours'].sum().reset_index()
        self.df = self.df.merge(self.hr_size, how='left', left_on=['Team'],
                               right_on=['Team'])
        self.df['Overtime per employee'] = self.df['Overtime_Hours'].div(self.df['number_of_people'])
        self.df.drop(columns=['Overtime_Hours', 'number_of_people'], inplace=True)

class Satisfaction(Metric):
    def __init__(self, hr):
        super().__init__('Satisfaction', hr, 'Satisfaction per employee')

    def group_and_count(self):
        self.df = self.df.groupby('Team')['Employee_Satisfaction_Score'].sum().reset_index()
        self.df = self.df.merge(self.hr_size, how='left', left_on=['Team'],
                                right_on=['Team'])
        self.df['Satisfaction per employee'] = self.df['Employee_Satisfaction_Score'].div(self.df['number_of_people'])
        self.df.drop(columns=['Employee_Satisfaction_Score', 'number_of_people'], inplace=True)

class Sickness(Metric):
    def __init__(self, hr):
        super().__init__('Sickness', hr, 'Sickness per employee')

    def group_and_count(self):
        self.df = self.df.groupby('Team')['Sick_Days'].sum().reset_index()
        self.df = self.df.merge(self.hr_size, how='left', left_on=['Team'],
                                right_on=['Team'])
        self.df['Sickness per employee'] = self.df['Sick_Days'].div(self.df['number_of_people'])
        self.df.drop(columns=['Sick_Days', 'number_of_people'], inplace=True)


class Training(Metric):
    def __init__(self, hr):
        super().__init__('Training', hr, 'Training per employee')

    def group_and_count(self):
        self.df = self.df.groupby('Team')['Training_Hours'].sum().reset_index()
        self.df = self.df.merge(self.hr_size, how='left', left_on=['Team'],
                                right_on=['Team'])
        self.df['Training per employee'] = self.df['Training_Hours'].div(self.df['number_of_people'])
        self.df.drop(columns=['Training_Hours', 'number_of_people'], inplace=True)

class Workload(Metric):
    def __init__(self, hr):
        super().__init__('Workload', hr, 'Workload per employee')

    def group_and_count(self):
        self.df = self.df.groupby('Team')['Projects_Handled'].sum().reset_index()
        self.df = self.df.merge(self.hr_size, how='left', left_on=['Team'],
                                right_on=['Team'])
        self.df['Workload per employee'] = self.df['Projects_Handled'].div(self.df['number_of_people'])
        self.df.drop(columns=['Projects_Handled', 'number_of_people'], inplace=True)

def metric_factory(type, hr):
    localizers = {
        "overtime": Overtime,
        "satisfaction": Satisfaction,
        "sickness": Sickness,
        "training": Training,
        "workload": Workload
    }
    return localizers[type](hr)


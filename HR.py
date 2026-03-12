import pandas as pd

# Loads a complete nominal roll of all employees and their team assignments.
class HR:
    def __init__(self, team_level):
        self.id_team = None
        self.number_of_people_team = None
        self.team_level = team_level
        self.load_HR_data()
        
    def load_HR_data(self):
        id_team = pd.read_csv('data/HR.csv')[['Employee_ID', self.team_level]]
        number_of_people_team = id_team.groupby([self.team_level]).count().reset_index()

        self.number_of_people_team = number_of_people_team.rename(columns={"Employee_ID": "number_of_people",
                                                                           self.team_level: "Team"})
        self.id_team = id_team.rename(columns={self.team_level: "Team"})
        print("Finished loading {} HR data".format(self.team_level))

    def get_id_team_data(self):
        return self.id_team

    def get_number_of_people_team(self):
        return self.number_of_people_team
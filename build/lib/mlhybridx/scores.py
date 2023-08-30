from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import numpy as np
import time

def typer(output, delay = 0.0001):
        for char in output:
                print(char, end="", flush= True)
                time.sleep(delay)
        print()
        return ""

def SE(y_test,y_pred, scr):
            if scr == "MSE":
                output1 = "R2 Score = ", r2_score(y_test,y_pred)
                output2 = f"MSE = {mean_squared_error(y_test,y_pred)}"
                ou1 = typer(output1)
                print(ou1)
            elif scr == "MAE":
                output1 = "R2 Score = ", r2_score(y_test,y_pred)
                output2 = f"MAE = {mean_absolute_error(y_test,y_pred)}"
                ou1 = typer(output1)
                print(ou1)
            elif scr == "RMSE":
                output1 = "R2 Score = ", r2_score(y_test,y_pred)
                output2 = f"RMSE = {np.sqrt(mean_squared_error(y_test,y_pred))}"
                ou1 = typer(output1)
                print(ou1)
            else:
                output1 = "R2 Score = ", r2_score(y_test,y_pred)
                output2 = "SE method's parameter must be 'MSE' , 'MAE' or 'RMSE'"
                ou1 = typer(output1)
                print(ou1)
            return typer(output2)
        

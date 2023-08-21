from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import numpy as np
import time

def typer(self, output, delay = 0.001):
        for char in output:
                print(char, end="", flush= True)
                time.sleep(delay)
        print()
        return None

def SE(y_test,y_pred, scr):
            if scr == "MSE":
                output1 = "R2 Score = ", r2_score(y_test,y_pred)
                typer(output1)
                output2 = f"MSE = {mean_squared_error(y_test,y_pred)}"
                return output2
            elif scr == "MAE":
                output1 = "R2 Score = ", r2_score(y_test,y_pred)
                typer(output1)
                output2 = f"MSE = {mean_absolute_error(y_test,y_pred)}"
                return output2
            elif scr == "RMSE":
                output1 = "R2 Score = ", r2_score(y_test,y_pred)
                typer(output1)
                output2 = f"MSE = {np.sqrt(mean_squared_error(y_test,y_pred))}"
                return output2
            else:
                output1 = "R2 Score = ", r2_score(y_test,y_pred)
                output2 = "SE method's parameter must be 'MSE' , 'MAE' or 'RMSE'"
            return output2
  

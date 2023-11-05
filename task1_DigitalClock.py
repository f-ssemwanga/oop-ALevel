class Clock:
  '''Class definition for the digital clock class'''
  def __init__(self, currentHour, currentMinute) -> None:
    '''Constructor method'''
    self.__hours = currentHour
    self.__minutes = currentMinute
    
  def setHour(self, currentHour):
    '''setter method for the private attribute hours '''
    self.__hours = currentHour
  def setMinute(self, currentMinute):
    '''setter method for the private attribute minutes '''
    self.__minutes = currentMinute
  
  def displayTime(self):
    '''outputs the hours concatenated with the minutes'''
    print(f'{self.__hours}:{self.__minutes}')
    
class Clock:
  '''Class definition for the digital clock class'''
  def __init__(self, currentHour: int, currentMinute: int) -> None:
    '''Constructor method'''
    self.__hours = currentHour
    self.__minutes = currentMinute
    
  def setHour(self, currentHour):
    '''setter method for the private attribute hours '''
    self.__hours = currentHour
  def setMinute(self, currentMinute):
    '''setter method for the private attribute minutes '''
    self.__minutes = currentMinute
  def newMinute(self):
    '''method to adjust the minutes'''
    if self.__minutes +1 < 60:
      self.__minutes = self.__minutes+1
    else:
      self.__minutes = 0
      self.newHour()
    
  def newHour(self):
    '''Method to adjust the hours'''
    if self.__hours +1 < 24:
      self.__hours += 1
    else:
      self.__hours = 0
  
  def displayTime(self):
    '''outputs the hours concatenated with the minutes'''
    print(f'{self.__hours:02d}:{self.__minutes:02d}')

myclock = Clock(10,55)
myclock.displayTime()
    
  
# -*- coding: utf-8 -*-

import numpy as np
import os,sys,time

class TicTacToeEnv:
 def __init__(self):
  self.board = None
  self.current_player = None
  self.result = None
  self.reset()

 def reset(self):
  self.board = np.zeros(16, dtype=np.int32)
  self.board[0] = 2
  self.board[7] = 2
  self.board[9] = 2
  self.current_player = "x"

 def step(self, index):
  if self.board[index] != 0:
   print("Invalid move!!")
   return None, None, None, {"valid": False}
  elif self.current_player == "x":
   self.board[index] = 1
   self.current_player = "o"
  else:
   self.board[index] = -1
   self.current_player = "x"
  observation = np.array(self.board)
  done,info = self.check_game_result()
  reward = 0
  return observation, reward, done, info

 def render(self):
  markers = []
  for i in self.board:
   if i == 0:
    markers.append("ー")
   elif i == 1:
    markers.append("✖")
   elif i == 2:
    markers.append("＊")
   else:
    markers.append("●")

  print("{} is thinking...".format(self.current_player))
  print("{0}\t{1}\t{2}\t{3}".format(markers[0], markers[1], markers[2],markers[3]))
  print("{0}\t{1}\t{2}\t{3}".format(markers[4], markers[5],markers[6], markers[7]))
  print("{0}\t{1}\t{2}\t{3}".format(markers[8], markers[9],markers[10], markers[11]))
  print("{0}\t{1}\t{2}\t{3}\n".format(markers[12], markers[13],markers[14], markers[15]))

 def check_game_result(self):
  x_win, o_win, is_full = False, False, False
  if np.sum(self.board[[1,2,3]]) == -3 or np.sum(self.board[[4, 5, 6]]) == -3 or np.sum(self.board[[12, 13, 14]]) == -3: 
   o_win = True  
  if np.sum(self.board[[13, 14, 15]]) == -3 or np.sum(self.board[[4, 8, 12]]) == -3 or np.sum(self.board[[2, 6, 10]]) == -3:
   o_win = True 
  if np.sum(self.board[[6, 10, 14]]) == -3 or np.sum(self.board[[1, 6, 11]]) == -3 or np.sum(self.board[[5, 10, 15]]) == -3:
   o_win = True 
  if np.sum(self.board[[2, 5, 8]]) == -3:  
   o_win = True
  if np.sum(self.board[[1,2,3]]) == 3 or np.sum(self.board[[4, 5, 6]]) == 3 or np.sum(self.board[[12, 13, 14]]) == 3: 
   x_win = True  
  if np.sum(self.board[[13, 14, 15]]) == 3 or np.sum(self.board[[4, 8, 12]]) == 3 or np.sum(self.board[[2, 6, 10]]) == 3: 
   x_win = True 
  if np.sum(self.board[[6, 10, 14]]) == 3 or np.sum(self.board[[1, 6, 11]]) == 3 or np.sum(self.board[[5, 10, 15]]) == 3:
   x_win = True 
  if np.sum(self.board[[2, 5, 8]]) == 3:  
   x_win = True 
  if 0 not in self.board:
   is_full = True
  done = x_win or o_win or is_full
  info = {"x": x_win, "o": o_win, "full": is_full, "valid": True}
  return done, info


	

 





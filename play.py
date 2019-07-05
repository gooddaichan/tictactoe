import sys
import numpy as np
import tensorflow as tf
import tictactoe

env = tictactoe.TicTacToeEnv()
observation = env.reset()
done = False
info = None

e='easy'
n='normal'
h='hard'
change=input()
if change==e:
 with tf.Graph().as_default() as g:
     sess = tf.Session()
     meta_graph = tf.saved_model.loader.load(
         sess=sess,
         tags=[tf.saved_model.tag_constants.SERVING],
         export_dir="model1"
     )
     model_signature = meta_graph.signature_def[tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
     input_signature = model_signature.inputs
     output_signature = model_signature.outputs
     # Get names of input and output tensors
     input_tensor_name = input_signature["x"].name
     output_tensor_name = output_signature["y"].name
     # Get input and output tensors
     x_ph = sess.graph.get_tensor_by_name(input_tensor_name)
     y = sess.graph.get_tensor_by_name(output_tensor_name)

if change==n:
 with tf.Graph().as_default() as g:
     sess = tf.Session()
     meta_graph = tf.saved_model.loader.load(
         sess=sess,
         tags=[tf.saved_model.tag_constants.SERVING],
         export_dir="model3"
     )
     model_signature = meta_graph.signature_def[tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
     input_signature = model_signature.inputs
     output_signature = model_signature.outputs
     # Get names of input and output tensors
     input_tensor_name = input_signature["x"].name
     output_tensor_name = output_signature["y"].name
     # Get input and output tensors
     x_ph = sess.graph.get_tensor_by_name(input_tensor_name)
     y = sess.graph.get_tensor_by_name(output_tensor_name)
if change==h:
 with tf.Graph().as_default() as g:
     sess = tf.Session()
     meta_graph = tf.saved_model.loader.load(
         sess=sess,
         tags=[tf.saved_model.tag_constants.SERVING],
         export_dir="model5"
     )
     model_signature = meta_graph.signature_def[tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
     input_signature = model_signature.inputs
     output_signature = model_signature.outputs
     # Get names of input and output tensors
     input_tensor_name = input_signature["x"].name
     output_tensor_name = output_signature["y"].name
     # Get input and output tensors
     x_ph = sess.graph.get_tensor_by_name(input_tensor_name)
     y = sess.graph.get_tensor_by_name(output_tensor_name)
 

for _ in range(16):
  env.render()
  if done:
   if info["x"]:
    print("x win!")
   elif info["o"]:
    print("o win!")
   else:
    print("Draw!")
   break
  # Compute scores
  prob_x_win = -np.ones(16)
  prob_o_win = np.ones(16)
 # prob_draw = np.zeros(9)
  for i in range(16):
   if env.board[i] == 0:
    board_copy = np.array([env.board])
    board_copy[0][i] = 1
    prob = sess.run(y, feed_dict={x_ph: board_copy})
    # print i, prob
    prob_x_win[i] = prob[0][0]
    prob_o_win[i] = prob[0][1]
    # prob_draw = prob[0][2]
    # Decide CPU's move
  if max(prob_x_win) >= 0.05:
   cpu_move = prob_x_win.argmax()
  else: 
   cpu_move = prob_o_win.argmin()
  _,_,done,info=env.step(cpu_move)
  env.render()
  if done:
   if info["x"]:
    print("x win!")
   elif info["o"]:
    print("o win!")
   else:
    print("Draw!")
   break
  while True:
   sys.stdout.write("Input your move: ")
   player_move = int(input())
   _, _, done, info = env.step(player_move)
   if info["valid"]:
    break






# Baxter-robot

###### First time to setup

mkdir -p $HOME/workspace/src

git clone --recursive https://github.com/rojas70/learning_ros_external_pkgs_noetic.git

git clone --recursive https://github.com/rojas70/learning_ros_noetic.git

git clone --recursive https://github.com/AlexLam616/Baxter-robot.git

###### Running the simulation
> Terminal 1: Running an empty baxter world

- cd $HOME/workspace

- ./baxter.sh

- roslaunch baxter_gazebo baxter_world.launch           

<br/>

> Terminal 2: Adding a table and a upright coke can

- cd $HOME/workspace

- ./baxter.sh

- roslaunch exmpl_models add_table_and_coke_can.launch

<br/>

> Terminal 3: Runnning baxter object grabber nodes

- cd $HOME/workspace

- ./baxter.sh

- roslaunch baxter_launch_files baxter_object_grabber_nodes.launch

<br/>

> Terminal 4: Runnning object grabber action client

- cd $HOME/workspace

- ./baxter.sh

- rosrun object_grabber example_object_grabber_action_client

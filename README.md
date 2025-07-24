

## Usage

This code requires CUDA, so you can open it in GoogleCollab

**Step 1:** Download the source codes. For example,
~~~bash
!git clone https://github.com/alina2002200/lithosim
~~~

**Step 2:** Go to the project root and unzip the environment
~~~bash
%cd lithosim
!unzip env.zip
~~~

**Step 3:** Conduct this code to create mask
~~~bash
%cd additional
!python image_generator_dots.py
~~~
If you want to add your own mask save it as lithosim/output/refine_net_output/t1_0_mask.png
See mask saved in lithosim/output/refine_litho_out/t1_0_mask.png

**Step 4**
Now to implement lithosim use this commands
~~~bash
%cd ..
%cd lithosim
!python run_litho_sim_batch.py
~~~
**Step 4**
To see difference between test image and lithosim
~~~bash
%cd ..
%cd additional
!python dots_vs_lithosim_dots.py
~~~

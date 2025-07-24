

## Usage
**Step 1:** Download the source codes. For example,
~~~bash
$ git clone https://github.com/alina2002200/lithosim
~~~

**Step 2:** Go to the project root and unzip the environment
~~~bash
$ cd lithosim/
$ unzip env.zip
~~~

**Step 3:** Conduct Neural-ILT on [ICCAD 2013 mask optimization contest benchmarks](https://ieeexplore.ieee.org/document/6691131)
Add mask as lithosim/output/refine_net_output/t1_0_mask.png
~~~bash
$ cd lithosim/
$ python run_litho_sim_batch.py
~~~
See mask in lithosim/output/refine_litho_out/t1_0_mask.png

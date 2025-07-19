# Neural-ILT
Neural-ILT is an end-to-end learning-based mask optimization tool developed by the research team supervised by Prof. Evangeline F.Y. Young in The Chinese University of Hong Kong (CUHK). Neural-ILT attempts to replace the conventional end-to-end ILT (inverse lithography technology) correction process under a holistic learning-based framework. It conducts on-neural-network ILT correction for the given layout under the guidiance of a partial coherent imaging model and directly outputs the optimized mask at the convergence.

Compared to the conventional academia ILT solutions, e.g., [MOSAIC](https://ieeexplore.ieee.org/document/6881379) (Gao *et al.*, DAC'14) and [GAN-OPC](https://ieeexplore.ieee.org/document/8465816) (Yang *et al.*, TCAD'20), Neural-ILT enjoys:
- much faster ILT correction process (20x ~ 70x runtime speedup)
- better mask printability at convergence
- modular design for easy customization and upgradation
- ...

More details are in the following papers:
* Jiang, Bentian, Lixin Liu, Yuzhe Ma, Hang Zhang, Bei Yu, and Evangeline FY Young. "[Neural-ILT: migrating ILT to neural networks for mask printability and complexity co-optimization](https://ieeexplore.ieee.org/abstract/document/9256592)", in 2020 IEEE/ACM International Conference On Computer Aided Design (ICCAD), pp. 1-9. IEEE, 2020.
* Jiang, Bentian, Xiaopeng Zhang, Lixin Liu, and Evangeline FY Young. "[Building up End-to-end Mask Optimization Framework with Self-training](https://dl.acm.org/doi/abs/10.1145/3439706.3447050)", in Proceedings of the 2021 International Symposium on Physical Design (ISPD), pp. 63-70. 2021.
* In submission to IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD).

## Requirements
-   python: [3.7.3](https://www.python.org/downloads/)
-   pytorch: [1.8.0](https://pytorch.org/)
-   torchvision: [0.2.2](https://pytorch.org/)
-   cudatoolkit: [11.1.1](https://developer.nvidia.com/cuda-toolkit)
-   pillow: [6.1.0](https://pypi.org/project/Pillow/)
-   GPU: >= 10GB GPU memory for pretrain, >= 7GB for Neural-ILT

## Usage
**Step 1:** Download the source codes. For example,
~~~bash
$ git clone https://github.com/cuhk-eda/neural-ilt.git
~~~

**Step 2:** Go to the project root and unzip the environment
~~~bash
$ cd Neural-ILT/
$ unzip env.zip
~~~
(Optional) To replace the ICCAD'20 training dataset with the ISPD'21 training dataset (last batch)
~~~bash
$ cd Neural-ILT/dataset/
$ unzip ispd21_train_dataset.zip
~~~

**Step 3:** Conduct Neural-ILT on [ICCAD 2013 mask optimization contest benchmarks](https://ieeexplore.ieee.org/document/6691131)
~~~bash
$ cd Neural-ILT/
$ python neural_ilt.py
~~~
Note that we observed minor variation (±0.5%) on mask printability score (L2+PVB, [statistics of 50 rounds](./stat/variation_test_neural_ilt.xlsx)). We haven't yet located the source of non-determinism. We would appreciate any insight from the community for resovling this non-determinism :sparkles:.

**Step 4 (optional):** Backbone model pre-training
~~~bash
$ cd Neural-ILT/
$ python pretrain_model.py
~~~

**Evaluation:** Evaluate the mask printability
~~~bash
$ cd Neural-ILT/
$ python eval.py --layout_root [root_to_layout_file] --layout_file_name [your_layout_file_name] --mask_root [root_to_mask_file] --mask_file_name [your_mask_file_name]
~~~

### Parameters
```angular2html
 |── neural_ilt.py
 |   ├── device/gpu_no: the device id
 |   ├── load_model_name/ilt_model_path: the pre-trained model of Neural-ILT
 |   ├── lr: initial learning rate
 |   ├── refine_iter_num: maximum on-neural-network ILT correction iterations
 |   ├── beta: hyper-parameter for cplx_loss in the Neural-ILT objective
 |   ├── gamma: lr decay rate
 |   ├── step_size: lr decay step size
 |   ├── bbox_margin: the margin of the crop bbox
 |
 |── pretrain_model.py
 |   ├── gpu_no: the device id
 |   ├── num_epoch: number of training epochs
 |   ├── alpha: cycle loss weight for l2
 |   ├── beta: cycle loss weight for cplx
 |   ├── lr: initial learning rate
 |   ├── gamma: lr decay rate
 |   ├── step_size: lr decay step size
 |   ├── margin: the margin of the crop bbox
 |   ├── read_ref: read the pre-computed crop bbox for each layout
 |
 |── End
```

Expolre your own recipe for model pretraining and Neural-ILT. Have fun! :smile:




THIS FREE SOFTWARE IS PROVIDED BY THE AUTHOR "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR ANY CONTRIBUTOR BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, EFFECTS OF UNAUTHORIZED OR MALICIOUS NETWORK ACCESS; PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


# CCLMoff
Genome editing with the CRISPR/Cas9 system has revolutionized life and medical sciences, particularly in treating monogenic human genetic diseases, by offering long-term therapeutic effects from a single intervention. 
However, CRISPR/Cas9 can tolerate mismatches and DNA/RNA bulges at target sites, leading to unintended off-target effects that challenge gene-editing therapy development. 
Existing high-throughput detection and in silico prediction methods have boundaries, as they are typically constrained to specifically designed single guide RNAs (sgRNAs) and exhibit limited performance on unseen sgRNAs.
To overcome these limitations, we introduced CRISPR/Cas Language Model for off-target prediction (CCLMoff), a deep learning framework incorporating a pretrained language model from RNAcentral for off-target site prediction. CCLMoff leverages the RNA language model to extract mutual sequence information between sgRNA and target sites and is trained on an extensive dataset. This approach enabled CCLMoff to demonstrate superior performance compared to existing models, accurately identifying off-target sites and showing robust generalization across diverse Next-Generation Sequencing (NGS)-based detection datasets. Furthermore, CCLMoff's model interpretation results highlighted the significance of the seed region in off-target prediction, underscoring its advanced analytical capabilities. The development and success of CCLMoff pave the way for establishing a comprehensive, end-to-end in silico sgRNA design platform. This platform promises to enhance the precision and efficiency of sgRNA design, thereby advancing the application of CRISPR/Cas9 in therapeutic contexts and potentially transforming the landscape of gene-editing therapies. 

## Key Features
- **Pretrained Language Model**: Utilizes RNAcentral's pretrained language model for enhanced mutual sequence information extraction.
- **High Accuracy**: Superior performance in off-target site identification compared to existing models.
- **Generalization**: Robust results across diverse NGS-based detection datasets.
- **Interpretability**: Highlights the significance of the seed region in off-target prediction.

## Usage

To use the CCLMoff model in your own research or project, follow the steps below:

### Requirements
1. Python >= 3.7
2. Required packages can be found in `requirements.txt`

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/CCLMoff.git

# Navigate to the repository folder
cd CCLMoff

# Install the required dependencies
pip install -r requirements.txt
```

### Running the Model

1.	Prepare your input data: Ensure you have your sgRNA and target site sequences formatted correctly.
2.	Run the model using the my_model.py script:
```bash
python my_model.py --input <input_data>
```
## Dataset

The training dataset used for developing CCLMoff and model parameters can be accessed via Figshare. This dataset is essential for training and testing the model on various sgRNA and target site pairs.

- [Training Dataset on Figshare](https://doi.org/10.6084/m9.figshare.27080566.v1)


## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Contact
If you have any questions or comments about this repository, please open an issue or contact the repository owner.  
Weian Du (duwan@mail.sysu.edu.cn)

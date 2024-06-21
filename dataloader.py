import pandas as pd
from torch.utils.data.dataset import Dataset
from torch.utils.data.sampler import WeightedRandomSampler
import numpy as np

class DatasetFromCSV(Dataset):
    def __init__(self, csv_path,id, is_train):
        raw_data = pd.read_csv(csv_path)
        raw_data["sgRNA_seq"] = raw_data["sgRNA_seq"].astype(str)
        raw_data["off_seq"] = raw_data["off_seq"].astype(str)

        if(is_train): 
            raw_data=raw_data[raw_data['sgRNA_type']!=id]
        
        else:
            raw_data=raw_data[raw_data['sgRNA_type']==id]


        # For re-weighting
        raw_data = raw_data.sort_values(by=['label'], ascending=True)
        count = raw_data['label'].value_counts()
        self.class_num_list = count.tolist()

        self.data = raw_data
        self.labels = np.asarray(raw_data.loc[:, ["label"]])
        self.ids = np.asarray(raw_data.loc[:, ["id"]])
        

    def __getitem__(self, index):
        ids = self.ids[index]
        sgrna_seq = self.data.iloc[index]['sgRNA_seq']
        target_seq = self.data.iloc[index]['off_seq']
        label = self.data.iloc[index]['label']
        seq = sgrna_seq+'<sep>'+target_seq
        seq = seq.replace('_','-')
        sample = {'seq': seq, 'label':label, 'id':ids}
        return sample

    def __len__(self):
        return len(self.data.index)



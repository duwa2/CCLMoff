import sys
sys.path.append("/mnt/")

from rnafm.fm import pretrained as rnapretrained
import torch
import torch.nn as nn

class ProtRNA(nn.Module):
    def __init__(self):
        super().__init__()

        self.rna_model, self.rna_alphabet = rnapretrained.esm1b_rna_t12()


        self.dense1 = nn.Linear(640, 64)
        self.dense2 = nn.Linear(64, 1)
        self.dropout = nn.Dropout(0.2)
        self.act =nn.Sigmoid()
        self.elu=nn.ELU()

        for m in self.children():
            if isinstance(m, nn.Linear):
                print(m)
                torch.nn.init.kaiming_uniform_(m.weight.data)
                # torch.nn.init.normal_(m.weight.data,0,0.1)
                # m.bias.data.fill_(0.0)
    
    def get_alphabet(self):
        return self.rna_alphabet

    def forward(self, tokens):
        rna_results=self.rna_model(tokens, repr_layers=[12], return_contacts=True)
        seq_emb=rna_results["representations"][12]
        seq_emb=seq_emb[:,0,:]

        dense1=self.elu(self.dropout(self.dense1(seq_emb)))
        dense2=self.dense2(self.dropout(dense1))
        out=self.act(dense2)

        return out


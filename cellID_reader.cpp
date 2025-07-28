#include <TROOT.h>
#include "TMath.h"
#include <iostream>
#include "TTree.h"
#include "TLegend.h"

void cellID_reader(){

  TChain *ch = new TChain("DecayTree");
  ch->Add("/eos/lhcb/user/i/ibachill/ntuples_PostCalibration/BdToKstGamma_skim_24c*.root");
  cout << " Open ntuple..." << endl;

  UInt_t runnumber = 305375;
  UInt_t  v_Region =-999;
  UInt_t  v_Row =-999;
  UInt_t  v_Column =-999;
  UInt_t  v_RUNNUMBER =0;
  UInt_t  v_ID =0;
  
  ch->SetBranchStatus("*", false);
  ch->SetBranchStatus("RUNNUMBER", true);
  ch->SetBranchAddress("RUNNUMBER", &v_RUNNUMBER);
  ch->SetBranchStatus("gamma_CaloNeutralArea", true);
  ch->SetBranchAddress("gamma_CaloNeutralArea", &v_Region);
  ch->SetBranchStatus("gamma_CaloNeutralRow", true);
  ch->SetBranchAddress("gamma_CaloNeutralRow", &v_Row);
  ch->SetBranchStatus("gamma_CaloNeutralCol", true);
  ch->SetBranchAddress("gamma_CaloNeutralCol", &v_Column);
  ch->SetBranchAddress("gamma_CaloNeutralID", &v_ID);

  Long64_t nentries = ch->GetEntries();

for (Long64_t jentry = 0; jentry < nentries; jentry++) {
    ch->GetEntry(jentry);

    if (v_RUNNUMBER == runnumber) {
        if (v_Region == 0 && v_Column == 33 && 
            (v_Row == 6 || v_Row == 7 || v_Row == 8 || v_Row == 9)) {
                cout << "CellID :" << v_ID << endl;
                
            }
    }
}

}
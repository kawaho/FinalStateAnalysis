'''

Ntuple branch template sets for trigger selections

Each string is transformed into an expression on a FinalStateEvent object.

Author: Evan K. Friis

IMPORTANT NOTE: If you want the logical OR of several paths, separate them 
by '|' rather than by ','. 
(When the Smart Trigger gets a group of paths separated by commas, it uses 
the one with the lowest prescale (taking the first in case of a tie).

'''

from FinalStateAnalysis.Utilities.cfgtools import PSet

_trig_template = PSet(
    namePass = 'evt.hltResult("paths")',
    nameGroup = 'evt.hltGroup("paths")',
    namePrescale = 'evt.hltPrescale("paths")',
)

singleLepton_25ns_MC = PSet(
    _trig_template.replace(
        name='IsoMu24',
        paths=r'HLT_IsoMu24_v\\d+'
        ),
    _trig_template.replace(
        name='Mu50',
        paths=r'HLT_Mu50_v\\d+'
        ),
    _trig_template.replace(
        name='Mu100',
        paths=r'HLT_OldMu100_v\\d+'
        ),
    _trig_template.replace(
        name='TkMu100',
        paths=r'HLT_TkMu100_v\\d+'
        ),
    _trig_template.replace(
        name='Ele27WPTight',
        paths=r'HLT_Ele27_WPTight_Gsf_v\\d+'
        ),
    _trig_template.replace(
        name='Ele32WPTight',
        paths=r'HLT_Ele32_WPTight_Gsf_v\\d+'
        ),
    _trig_template.replace(
        name='Ele35WPTight',
        paths=r'HLT_Ele35_WPTight_Gsf_v\\d+'
        ),
    )

singleLepton_25ns = PSet(
    _trig_template.replace(
        name='IsoMu24',
        paths=r'HLT_IsoMu24_v\\d+'
        ),
    _trig_template.replace(
        name='Mu50',
        paths=r'HLT_Mu50_v\\d+'
        ),
    _trig_template.replace(
        name='Mu100',
        paths=r'HLT_OldMu100_v\\d+'
        ),
    _trig_template.replace(
        name='TkMu100',
        paths=r'HLT_TkMu100_v\\d+'
        ),
    _trig_template.replace(
        name='Ele27WPTight',
        paths=r'HLT_Ele27_WPTight_Gsf_v\\d+'
        ),
    _trig_template.replace(
        name='Ele32WPTight',
        paths=r'HLT_Ele32_WPTight_Gsf_v\\d+'
        ),
    _trig_template.replace(
        name='Ele35WPTight',
        paths=r'HLT_Ele35_WPTight_Gsf_v\\d+'
        ),
    )

doubleLepton_25ns = PSet(
    _trig_template.replace(
        name='mu12e23DZ',
        paths=r'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v\\d+'
        ),
    _trig_template.replace(
        name='mu12e23',
        paths=r'HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_v\\d+'
        ),
    _trig_template.replace(
        name='mu23e12DZ',
        paths=r'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v\\d+'
        ),
    _trig_template.replace(
        name='mu23e12',
        paths=r'HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v\\d+'
        ),
    _trig_template.replace(
        name='mu8e23',
        paths=r'HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v\\d+'
        ),
    _trig_template.replace(
        name='doubleMuDZminMass3p8',
        paths=r'HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v\\d+'
        ),
    _trig_template.replace(
        name='doubleE_23_12',
        paths=r'HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v\\d+'
        ),
    _trig_template.replace(
        name='doubleE25',
        paths=r'HLT_DoubleEle25_CaloIdL_MW_v\\d+'
        ),
    _trig_template.replace(
        name='Ele24LooseTau30',
        paths=r'HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Ele24LooseTau30TightID',
        paths=r'HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTau30_eta2p1_TightID_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Ele24MediumTau30',
        paths=r'HLT_Ele24_eta2p1_WPTight_Gsf_MediumChargedIsoPFTau30_eta2p1_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Ele24MediumTau30TightID',
        paths=r'HLT_Ele24_eta2p1_WPTight_Gsf_MediumChargedIsoPFTau30_eta2p1_TightID_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Ele24TightTau30',
        paths=r'HLT_Ele24_eta2p1_WPTight_Gsf_TightChargedIsoPFTau30_eta2p1_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Ele24TightTau30TightID',
        paths=r'HLT_Ele24_eta2p1_WPTight_Gsf_TightChargedIsoPFTau30_eta2p1_TightID_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Ele24LooseHPSTau30',
        paths=r'HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Ele24LooseHPSTau30TightID',
        paths=r'HLT_Ele24_eta2p1_WPTight_Gsf_LooseChargedIsoPFTauHPS30_eta2p1_TightID_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Ele24MediumHPSTau30',
        paths=r'HLT_Ele24_eta2p1_WPTight_Gsf_MediumChargedIsoPFTauHPS30_eta2p1_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Ele24MediumHPSTau30TightID',
        paths=r'HLT_Ele24_eta2p1_WPTight_Gsf_MediumChargedIsoPFTauHPS30_eta2p1_TightID_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Ele24TightHPSTau30',
        paths=r'HLT_Ele24_eta2p1_WPTight_Gsf_TightChargedIsoPFTauHPS30_eta2p1_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Ele24TightHPSTau30TightID',
        paths=r'HLT_Ele24_eta2p1_WPTight_Gsf_TightChargedIsoPFTauHPS30_eta2p1_TightID_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Mu20LooseTau27',
        paths=r'HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Mu20LooseTau27TightID',
        paths=r'HLT_IsoMu20_eta2p1_LooseChargedIsoPFTau27_eta2p1_TightID_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Mu20MediumTau27',
        paths=r'HLT_IsoMu20_eta2p1_MediumChargedIsoPFTau27_eta2p1_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Mu20MediumTau27TightID',
        paths=r'HLT_IsoMu20_eta2p1_MediumChargedIsoPFTau27_eta2p1_TightID_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Mu20TightTau27',
        paths=r'HLT_IsoMu20_eta2p1_TightChargedIsoPFTau27_eta2p1_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Mu20TightTau27TightID',
        paths=r'HLT_IsoMu20_eta2p1_TightChargedIsoPFTau27_eta2p1_TightID_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Mu20LooseHPSTau27',
        paths=r'HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Mu20LooseHPSTau27TightID',
        paths=r'HLT_IsoMu20_eta2p1_LooseChargedIsoPFTauHPS27_eta2p1_TightID_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Mu20MediumHPSTau27',
        paths=r'HLT_IsoMu20_eta2p1_MediumChargedIsoPFTauHPS27_eta2p1_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Mu20MediumHPSTau27TightID',
        paths=r'HLT_IsoMu20_eta2p1_MediumChargedIsoPFTauHPS27_eta2p1_TightID_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Mu20TightHPSTau27',
        paths=r'HLT_IsoMu20_eta2p1_TightChargedIsoPFTauHPS27_eta2p1_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='Mu20TightHPSTau27TightID',
        paths=r'HLT_IsoMu20_eta2p1_TightChargedIsoPFTauHPS27_eta2p1_TightID_CrossL1_v\\d+'
        ),
    _trig_template.replace(
        name='DoubleMediumTau35',
        paths=r'HLT_DoubleMediumChargedIsoPFTau35_Trk1_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='DoubleMediumTau35TightID',
        paths=r'HLT_DoubleMediumChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='DoubleTightTau35TightID',
        paths=r'HLT_DoubleTightChargedIsoPFTau35_Trk1_TightID_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='DoubleTightTau35',
        paths=r'HLT_DoubleTightChargedIsoPFTau35_Trk1_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='DoubleMediumTau40',
        paths=r'HLT_DoubleMediumChargedIsoPFTau40_Trk1_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='DoubleMediumTau40TightID',
        paths=r'HLT_DoubleMediumChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='DoubleTightTau40',
        paths=r'HLT_DoubleTightChargedIsoPFTau40_Trk1_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='DoubleTightTau40TightID',
        paths=r'HLT_DoubleTightChargedIsoPFTau40_Trk1_TightID_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='DoubleMediumHPSTau35',
        paths=r'HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='DoubleMediumHPSTau35TightID',
        paths=r'HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_TightID_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='DoubleTightHPSTau35TightID',
        paths=r'HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_TightID_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='DoubleTightHPSTau35',
        paths=r'HLT_DoubleTightChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='DoubleMediumHPSTau40',
        paths=r'HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='DoubleMediumHPSTau40TightID',
        paths=r'HLT_DoubleMediumChargedIsoPFTauHPS40_Trk1_TightID_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='DoubleTightHPSTau40',
        paths=r'HLT_DoubleTightChargedIsoPFTauHPS40_Trk1_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='DoubleTightHPSTau40TightID',
        paths=r'HLT_DoubleTightChargedIsoPFTauHPS40_Trk1_TightID_eta2p1_Reg_v\\d+'
        ),
    _trig_template.replace(
        name='VBFDoubleTightHPSTau20',
        paths=r'HLT_VBF_DoubleLooseChargedIsoPFTauHPS20_Trk1_eta2p1_Reg_v\\d+'
        ),
    )

tripleLepton = PSet(
    _trig_template.replace(
        name='tripleE',
        paths=r'HLT_Ele16_Ele12_Ele8_CaloIdL_TrackIdL_v\\d+'
        ),
    _trig_template.replace(
        name='tripleMu12_10_5',
        paths=r'HLT_TripleMu_12_10_5_v\\d+'
        ),
    _trig_template.replace(
        name='dimu9ele9',
        paths=r'HLT_DiMu9_Ele9_CaloIdL_TrackIdL_DZ_v\\d+'
        ),
    )


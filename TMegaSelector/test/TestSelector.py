import ROOT
from FinalStateAnalysis.TMegaSelector.megaselect import TMegaPySelector

class TestSelector(TMegaPySelector):
    def Version(self):
        return 2
    def MegaSlaveBegin(self, tree):
        self.histo = ROOT.TH1F("adsf", "asdf", 100, 0, 100)
        #self.fOutput.Add(self.histo)
    def MegaProcess(self, entry):
        print entry
        self.histo.Fill(entry)
        return True
    def MegaSlaveTerminate(self):
        #self.fOutput.Add(self.histo)
        del self.histo

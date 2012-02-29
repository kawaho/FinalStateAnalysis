#!/usr/bin/env python

import os
import ROOT
from FinalStateAnalysis.TMegaSelector.megaselect import TMegaPySelector

proof = ROOT.TProof.Open('workers=4')
proof.SetParameter( "PROOF_UseTreeCache",  0 )
proof.SetLogLevel(0)
proof.SetRealTimeLog(1)
proof.Exec('gSystem->Load("$CMSSW_BASE/lib/$SCRAM_ARCH/libFinalStateAnalysisTMegaSelector.so")')
#proof.AddEnvVar('PROOF_INITCMD', "cat $CMSSW_BASE/src/FinalStateAnalysis/recipe/environment.sh")
#proof.AddEnvVar('CMSSW_BASE', os.environ['CMSSW_BASE'])

#proof.Exec(".! echo $CMSSW_BASE", 1)
#proof.Exec(".! echo $PATH", 1)

#proof.DelEnvVar('PATH')
##proof.AddEnvVar('PATH', os.environ['PATH'])
#proof.Exec(".! echo $PATH", 1)
#ROOT.TProof.AddEnvVar('WTF', "WTF")
#proof.Exec(".! echo $WTF", 1)

chain = ROOT.TChain("TestTree")
# test_file.root can be generated by the CPP unit test
chain.Add('test_file.root')
print "Got tree with %i entries" % chain.GetEntries()

dataset = ROOT.TDSet("doot", "TestTree", "/", "TTree")
dataset.Add('file:test_file.root')

#print "Running process"
#result = proof.Process(dataset, "TMegaPySelector", "TestSelector")
#print result
#dataset.Process("TMegaPySelector", "TestSelector")

#print "Analyze dataset"
#chain.Process("TPySelector", "TestPlainPySelector")

#print "Analyze dataset using MEGA"
#chain.Process("TMegaPySelector", "TestSelector")

print "Analyze dataset using TDSet"
dataset.Process("TMegaPySelector", "TestSelector")
#dataset.Draw("intBranch > 0")
#dataset.Process("TPySelector", "TestPlainPySelector")

#ROOT.TProof.Mgr("<master>").GetSessionLogs().Display("*")

print "Done"

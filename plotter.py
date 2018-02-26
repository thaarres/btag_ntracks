import ROOT as rt
import os,sys
from time import sleep

if len(sys.argv)>1: 
  f = sys.argv[1]
else:
  f = "RSGravitonToWWToQQQQ_M-700_TuneCUETP8M1_14TeV-pythia8_noPU.root"
  
if len(sys.argv)>2: 
  outn = sys.argv[2]
else:
  outn = "RSGravitonToWWToQQQQ_M-2000_PU200.root"
  

if __name__ == "__main__":
  print f
  # infile = rt.TFile(f,"READ")
  # print "Working on file", infile.GetName()
  # cmd = "edmDumpEventContent %s"%f
  # print cmd
  # os.system(cmd)

  # load FWlite python libraries
  from DataFormats.FWLite import Handle, Events
  from DataFormats.FWLite import Handle, Events

  handleak8PFJetsCHS, labelak8PFJetsCHS   = Handle ("std::vector<reco::PFJet>"),"ak8PFJetsCHS"
  handleak4PFJetsCHS, labelak4PFJetsCHS   = Handle ("std::vector<reco::PFJet>"),"ak4PFJetsCHS"
  handlePixelClusters, labelPixelClusters = Handle ("edmNew::DetSetVector<SiPixelCluster>"),"siPixelClusters"
  
  edm::ESHandle<TrackerGeometry> geom;
    es.get<TrackerDigiGeometryRecord>().get( geom );
    const TrackerGeometry& theTracker(*geom);

  events = Events(f)
  
  histPt = rt.TH1D("Jet_pt","Jet_pt",40,0.,2000.) #https://root.cern.ch/doc/master/classTH1.html
  for iev,event in enumerate(events): #This is each event
    if iev % 1000 == 0: print "Event", iev	
    event.getByLabel (labelPixelClusters, handlePixelClusters)
    event.getByLabel (labelak8PFJetsCHS, handleak8PFJetsCHS)
    event.getByLabel (labelak4PFJetsCHS, handleak4PFJetsCHS)
    PixelClusters = handlePixelClusters.product()
    AK8jets = handleak8PFJetsCHS.product()
    # import pdb; pdb.set_trace()
  #   for jet in AK8jets: #These are all the jets per event
  #     print "Jet transverse momentum:" ,jet.pt()
  #     histPt.Fill(jet.pt())
  #
  # c1 = rt.TCanvas("c1","c1",600,600) #https://root.cern.ch/doc/master/classTCanvas.html
  # c1.cd()
  # histPt.Draw()
  # c1.SetLogy()
  # c1.SaveAs("jetPt.png")
  #For debugging
    
    from Geometry.CommonTopologies.
    for clust in PixelClusters.data():
      print "Cluster x = " ,clust.x()
      print "Cluster y = " ,clust.y()
      
    theGeomDet = theTracker.idToDet(hit_detId) )
    topol = theGeomDet.specificTopology() 
      
      lp = topol.localPosition( MeasurementPoint( clust.x(), clust.y() ) )
      # lx = lp.x()
      # ly = lp.y()
      #
      # clustgp = theGeomDet.surface().toGlobal( lp )
      # double gX = clustgp.x()
      # double gY = clustgp.y()
      # gZ = clustgp.z()
      # v =  rt.TVector3(vgX,gY,gZ)
      # gPhi= v.Phi()#phi of the hit
      # gR = v.Perp()#r of the hit


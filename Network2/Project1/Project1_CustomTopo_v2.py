"""
Project1 Custom Topology

Author :‌ Maryam Saeedmehr
Std. NO. : 9629373

* How to establish it?
Just Run:

~$ sudo mn --custom Project1_CustomTopo_v2.py --topo sample

"""
from mininet.topo import Topo

class CustomTopo( Topo ):

    def __init__( self ):

        Topo.__init__( self)
        
        #hosts definition
        Host1 = self.addHost( 'h1' )
        Host2 = self.addHost( 'h2' )
        Host3 = self.addHost( 'h3' )
        Host4 = self.addHost( 'h4' )
        Host5 = self.addHost( 'h5' )
        Host6 = self.addHost( 'h6' )
        Host7 = self.addHost( 'h7' )
        Host8 = self.addHost( 'h8' )
        Host9 = self.addHost( 'h9' )
        Host10 = self.addHost( 'h10' )
        Host11 = self.addHost( 'h11' )
        Host12 = self.addHost( 'h12' )
        Host13 = self.addHost( 'h13' )
        Host14 = self.addHost( 'h14' )

        #switches definition
        Switch1 = self.addSwitch( 's1' )
        Switch2 = self.addSwitch( 's2' )
        Switch3 = self.addSwitch( 's3' )
        Switch4 = self.addSwitch( 's4' )
        Switch5 = self.addSwitch( 's5' )
        Switch6 = self.addSwitch( 's6' )
        Switch7 = self.addSwitch( 's7' )
        Switch8 = self.addSwitch( 's8' )
        Switch9 = self.addSwitch( 's9' )
        Switch10 = self.addSwitch( 's10' )
        Switch11 = self.addSwitch( 's11' )
        Switch12 = self.addSwitch( 's12' )

        #links definition
        self.addLink( Switch1, Switch2 )
        self.addLink( Switch1, Switch3 )
        self.addLink( Switch1, Switch4 )
        self.addLink( Switch2, Switch5 )
        self.addLink( Switch2, Switch6 )
        self.addLink( Switch3, Switch7 )
        self.addLink( Switch4, Switch8 )
        self.addLink( Switch4, Switch9 )
        self.addLink( Switch4, Switch10 )
        self.addLink( Switch5, Switch11 )
        self.addLink( Switch5, Switch12 )

        self.addLink( Host1, Switch1 )
        self.addLink( Host2, Switch1 )
        self.addLink( Host3, Switch3 )
        self.addLink( Host4, Switch5 )
        self.addLink( Host5, Switch6 )
        self.addLink( Host6, Switch7 )
        self.addLink( Host7, Switch7 )
        self.addLink( Host8, Switch8 )
        self.addLink( Host9, Switch9 )
        self.addLink( Host10, Switch9 )
        self.addLink( Host11, Switch10 )
        self.addLink( Host12, Switch11 )
        self.addLink( Host13, Switch11 )
        self.addLink( Host14, Switch12 )

topos = { 'sample' : ( lambda: CustomTopo())}


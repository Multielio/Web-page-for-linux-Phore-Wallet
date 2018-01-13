# -*- coding: utf-8 -*-
"""
Created on Wed Jan	3 18:11:39 2018

@author: Yo
"""

import subprocess	   
import json
import time
from datetime import datetime, timedelta
from time import gmtime, strftime


def gtime(sec):
	d = datetime(1,1,1) + timedelta(seconds=sec)
	return "%d day(s), %d hour(s), %d minute(s), %d second(s)" % (d.day-1, d.hour, d.minute, d.second)

web_path = "/var/www/html/p/{}"
web_page="""
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
<head>
  <title>Phore Linux Wallet Manager </title>
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css" type="text/css">
  <link rel="stylesheet" href="font-awesome-4.6.3/css/font-awesome.min.css" type="text/css">
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
  <link rel="stylesheet" href="style.css" type="text/css">
</head>
<body>
	<div class="container">
		<div class="jumbotron">
		<div class="page-header">
			<h2><img src="https://phore.io/wp-content/uploads/2017/10/phore-logo.png" alt="Phore" class="logo-default"> Linux Wallet Manager v0.1</h2>
		</div>
		</div>


		
		
		<div class="row">
			<div class="col-md-4">
			
				<i class="fa fa fa-money fa-3x" aria-hidden="true"></i>
					<a href="#/" class="btn btn-primary" >Balance:	{}</a>
	
	
			</div>
			<div class="col-md-4">
				<i class="fa fa-plus fa-3x" aria-hidden="true"></i><a href="#/" class= "btn btn-success" > 
					 {}
				</a>
			</div>
			<div class="col-md-4">
				<i class="fa fa-square fa-3x" aria-hidden="true"></i><a href="#/" class="btn btn-warning"> Blocks 
					{}
					
				</a>
			</div>

		</div>
		<hr>


		<i class="fa fa-clock-o fa-2x" aria-hidden="true"></i> 
		<h4>Wallet History</h4>
		<ul>
		{}
		</ul>
		<hr>



	   
	   <i class="fa fa-flask fa-2x" aria-hidden="true"></i><h4>Phore Network</h4>
		<ul>
		  <li> Difficulty : 
		  {}
		  </li>
		 <li> Total zPHR Supply:
		 {}
			
		</li>
		</ul>
		
		
		
	   
		<hr>
		<i class="fa fa-server fa-2x" aria-hidden="true"></i><h4> Masternode</h4>
	   
	   
	   <b> Some data : </b>
	   <ul>
	   <li>Online Masternode: {} </li>
	   <li>Time to next super block: {} </li>
	   </ul>
	   </br>
	   <b>Budget Proposal:</b>
	   <div>
		{}
	   </div>
		<hr>
	
		<h4>Usefull Links</h4>
		<ul>
			<li> <a href="https://phore.io/">Phore Official Website</a></li>
  
		</ul>

	</div>
	</br>
    </br>


</body>
<footer class="page-footer center-on-small-only stylish-color-dark">
<div class="footer-copyright">
        <div class="container-fluid">
            <p class="text-center"> By Multielio | My phore address: P8wYoLWebAXBKD6wTSMv1mxXeQRfM3JLom </p>

        </div>
</div>
</footer>
</html>


"""

#"""
#1. Balance
#2. Staking
#3. Block
#4. Difficulty
#5. zPHRsupply
#"""

mastpatern = """
		 <div class="col-sm-6">
		<div class="panel panel-default">
		<div class="panel-heading"><b>Projet Name: {}</b></div>
		<div class="panel-body">
		<ul>
		<li>URL : {}</li>
		<li>Hash : {}</li>
		<li>FeeHash : {}</li>
		<li>BlockStart : {}</li>
		<li>BlockEnd : {}</li>
		<li>TotalPaymentCount : {}</li>
		<li>RemainingPaymentCount : {}</li>
		<li>PaymentAddress : {}</li>
		<li>Ratio : {}</li>
		<li>TotalPayment : {}</li>
		<li>MonthlyPayment : {}</li>
		<i class="fa fa-check fa-1x" aria-hidden="true"></i><a href="#/" class= "btn btn-success" > {} YES</a>
		<i class="fa fa-times fa-1x" aria-hidden="true"></i><a href="#/" class= "btn btn-danger" > {} NO</a>
		 </ul>
		</div>
		</div>
		</div>"""

lasttime = time.time()
i=0
lastbalance = 0
while i ==0:
	if time.time()-lasttime >=60:
		lastime = time.time()
		
		#######################################################################################
		# GET DATA 
		#######################################################################################
		# Getting some info with phore-cli getinfo
		p = subprocess.Popen(["phore-cli","getinfo"], stdout=subprocess.PIPE)
		output, err = p.communicate()
		o = json.loads(output)
		
		#Getting info from phore-cli getbudgetinfo
		p = subprocess.Popen(["phore-cli","getbudgetinfo"], stdout=subprocess.PIPE)
		output, err = p.communicate()
		oo = json.loads(output)
		
		#Getting info from phore-cli getbudgetinfo
		p = subprocess.Popen(["phore-cli","getnextsuperblock"], stdout=subprocess.PIPE)
		ooo, err = p.communicate()
		
		#Getting info from phore-cli getmasternodecount
		p = subprocess.Popen(["phore-cli","getmasternodecount"], stdout=subprocess.PIPE)
		output, err = p.communicate()
		oooo = json.loads(output)
		
		#Getting info from phore-cli listtransactions
		p = subprocess.Popen(["phore-cli","listtransactions"], stdout=subprocess.PIPE)
		output, err = p.communicate()
		ooooo = json.loads(output)
		#######################################################################################
		# Creating data to display
		#######################################################################################
		## BUILDING MASTERNODE INFO	
		masternodestring =""
		l = 0
		for el in oo:
			mtext = mastpatern.format(el["Name"],el["URL"],el["Hash"],el["FeeHash"],el["BlockStart"],el["BlockEnd"],el["TotalPaymentCount"],el["RemainingPaymentCount"],el["PaymentAddress"],el["Ratio"],el["TotalPayment"],el["MonthlyPayment"],el["Yeas"],el["Nays"])
			if l%2 ==0:
				if l != len(el):
					masternodestring +="""</div><div class="row">"""+mtext 
				else:
					masternodestring +="""</div><div class="row">"""+mtext+"</div><div>"
			else:
				masternodestring +=mtext +"</div><div>"
			l+=1
			
		## BUILDING TRANSACTIONS
		trans = ""
		for el in ooooo:
			receive = """<li class="list-group-item list-group-item-success"> + {}	PHR <p class="text-right">[{}]</p></li>"""
			sent = """<li class="list-group-item list-group-item-danger">  {}	PHR <p class="text-right">[{}]</p></li>"""
			u = el["amount"]
			timet = el["time"]
			time_string = datetime.fromtimestamp(int(timet)).strftime('%Y-%m-%d %H:%M:%S')
			try:
				b = el["fee"]
				if round(float(b),2) ==  7:
					continue
			except:
				pass
			if float(u) <0:
				trans+= sent.format(u,time_string)
			else:
				trans += receive.format(u,time_string)
			
		newbalance = o["balance"]
		fo = open(web_path.format("phore.php"), "w")
		fo.write(web_page.format(o["balance"],o["staking status"],o["blocks"],trans,o["difficulty"],o["zPHRsupply"]["total"],oooo["total"],gtime(60*(int(ooo)-int(o["blocks"]))), masternodestring))
		fo.close()
		
			
			

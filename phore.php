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

		<div class="page-header">
			<h2><img src="https://phore.io/wp-content/uploads/2017/10/phore-logo.png" alt="Phore" class="logo-default"> Linux Wallet Manager v0.1</h2>
		</div>



		<div class="row">
			<div class="col-md-3">
			
				<i class="fa fa fa-money fa-3x" aria-hidden="true"></i>
					<a href="#/" class="btn btn-primary" >Balance:  
	
					<?php

					$data = file_get_contents('/var/www/html/phorec.json');

					$o = json_decode($data);
					echo $o->balance;
					?>
					
					</a>
	
			</div>
			<div class="col-md-3">
				<i class="fa fa-plus fa-3x" aria-hidden="true"></i><a href="#/" class= "btn btn-success" > 
					<?php

					$data = file_get_contents('/var/www/html/phorec.json');

					$o = json_decode($data);
					echo $o->{'staking status'};
					
					
					?>
				</a>
			</div>
			<div class="col-md-3">
				<i class="fa fa-square fa-3x" aria-hidden="true"></i><a href="#/" class="btn btn-warning"> Blocks 
					<?php

					$data = file_get_contents('/var/www/html/phorec.json');

					$o = json_decode($data);
					echo $o->blocks;
					?>
				</a>
			</div>
		</div>
		<hr>


		<i class="fa fa-clock-o fa-2x" aria-hidden="true"></i> 
		<h4>Wallet History</h4>
		<?php
			$file = "/var/www/html/history.txt";
			if(file_exists($file)){
				echo file_get_contents($file);
			}
		?>	

		<hr>



		<i class="fa fa-flask fa-2x" aria-hidden="true"></i><h4>Phore Network<h4>
		<ul>
		  <li> Difficulty : 
		  <?php

					$data = file_get_contents('/var/www/html/phorec.json');

					$o = json_decode($data);
					echo $o->difficulty;
					?>
		  </li>
		  
		</ul>
		
		<hr>
		<i class="fa fa-bar-chart fa-2x" aria-hidden="true"></i><h4>zPHR Supply<h4>
		<ul><li> Total:
			<?php

					$data = file_get_contents('/var/www/html/phorec.json');

					$o = json_decode($data);
					echo ($o->zPHRsupply)->total;
					?>
		</li>
		</ul>
		<hr>
		<h4>Usefull Links</h4>
		<ul>
			<li> <a href="https://phore.io/">Phore Official Website</a></li>
  
		</ul>

	</div>

</body>
</html>
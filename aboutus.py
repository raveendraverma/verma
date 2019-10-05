#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
	<head>
		<link href="css/bootstrap.min.css" rel="stylesheet" />
		<link href="css/bootstrap-theme.min.css" rel="stylesheet" />
		<script src="js/jquery.js" type="text/javascript" rel="javascript"></script>
		<script src="js/bootstrap.min.js"  type="text/javascript" rel="javascript"></script>
		<style>
		#outer
		{
		min-height:1300px;
		border:1px solid red;
		}
		#logo
		{
		min-height:200px;
		background-color:gray;
		}
		#pt
		{
		min-height:200px;
		background-color:lightblue;
		}
		#menu
		{
		min-height:50px;
		
		}
		#slider
		{
		min-height:300px;
		background-color:darkred;
		margin-top:-20px;
		}
		#main
		{
		  min-height:750px;
		  background-color:lightgray;
		}
		#lfooter
		{
		min-height:100px;
		background-color:lightyellow;
		}
		#rfooter
		{
		min-height:100px;
		background-color:lightgreen;
		}
		#my_ul li a
		{
		color:white;
		}
		#my_ul li a:hover
		{
		color:red;
		}
		#pt
		{
		font-size:50pt;
		padding-top:50px;
		font-weight:bold;
		}
		</style>
	</head>
	<body>
		<div class="container" id="outer">
		<!---  start header div--->
			<div class="row">
				<div class="col-sm-2" id="logo">
				<img src="images/logo.jpg" style="min-height:200px;min-width:200px;margin-left:-13px;"/>
				</div>
				<div class="col-sm-10 text-center" id="pt" ><span id="ptitle">E - Study Zone</span></div>
			</div>
			<!---  end header div--->
			<!---  start menu div--->
			<div class="row" >
				<div class="col-sm-12" id="menu" style="padding:0px;margin:0px;">
				<nav class="navbar navbar-default" style="border:none;">
  <div class="container-fluid" style="background-color:black;color:white;font-size:16pt;font-weight:bold;">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#"><span class="glyphicon glyphicon-align-justify" style="color:white;"></span></a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav" id="my_ul">
        <li ><a href="home.py">HOME <span class="sr-only">(current)</span></a></li>
        <li><a href="aboutus.py">ABOUTUS</a></li>
        <li><a href="contactus.py">CONTACTUS</a></li>
        <li><a href="enquiry.py">ENQUIRY</a></li>
        <li><a href="reg.py">REGISTRATION</a></li>
        <li><a href="login.py">LOGIN</a></li>
       <!-- <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">Action</a></li>
            <li><a href="#">Another action</a></li>
            <li><a href="#">Something else here</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">Separated link</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">One more separated link</a></li>
          </ul>
        </li> -->
		
      </ul>
      
     
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
				</div>
			</div>
			<!---  end menu div--->
			<!---  start slider div--->
			<div class="row"> 
				<div class="col-sm-12" id="slider" style="padding:0px;margin:0px;margin-top:-20px;">
				
				<div id="carousel-example-generic" class="carousel slide" data-ride="carousel">
  <!-- Indicators -->
  <ol class="carousel-indicators">
    <li data-target="#carousel-example-generic" data-slide-to="0" class="active"></li>
    <li data-target="#carousel-example-generic" data-slide-to="1"></li>
    <li data-target="#carousel-example-generic" data-slide-to="2"></li>
    <li data-target="#carousel-example-generic" data-slide-to="3"></li>
  </ol>

  <!-- Wrapper for slides -->
  <div class="carousel-inner" role="listbox">
    <div class="item active">
      <img src="images/b1.jpg" alt="...">
      <div class="carousel-caption">
        ...
      </div>
    </div>
    <div class="item">
      <img src="images/b2.jpg" alt="...">
      <div class="carousel-caption">
        ...
      </div>
    </div>
	 <div class="item">
      <img src="images/b3.jpg" alt="...">
      <div class="carousel-caption">
       
      </div>
    </div>
    <div class="item">
      <img src="images/b4.jpg" alt="...">
      <div class="carousel-caption">
       
      </div>
    </div>
  </div>

  <!-- Controls -->
  <a class="left carousel-control" href="#carousel-example-generic" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#carousel-example-generic" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
				</div>
			</div>
			<!---  end slider div--->
			<!---  start main div--->
			<div class="row">
			<div class="col-sm-12" id="main" style="margin-top:-40px;">
			<h2 class="text-center" style="color:darkred;font-weight:bold;">ABOUT-US Page</h2>
			<hr>
			
			</div>
			</div>
			<!---  end main div--->
			<!---  start footer div--->
			<div class="row">
				<div class="col-sm-6" id="lfooter"></div>
				<div class="col-sm-6" id="rfooter"></div>
			</div>
			<!---  end footer div--->
			
		</div> <!----end outer div  --->
	</body>
</html>




"""
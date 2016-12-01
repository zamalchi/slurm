<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="css/bootstrap.min.css"/>
 	<link rel="stylesheet" type="text/css" href="css/main.css" />

 	<link rel="shortcut icon" href="img/favicon.ico" />

 	<meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>


<body onload="anchorToRequested()">

% include('_navbar.tpl', states=states)

<!-- main container start -->
<div class="container" name="main">

<!-- outputs row start -->
<!-- % include('_outputs.tpl', anchor=anchor, states=states, node=node) -->
% include('_outputs.tpl')
<!-- outputs row end -->

</div>
<!-- main container end -->


<!-- ######################################################################################################### -->
<!-- SCRIPTS START -->	

	<!-- jquery must come first and is required by bootstrap -->
<script src="js/jquery-3.1.0.min.js"></script>
<script src="js/bootstrap.min.js"></script>

<!-- custom js functions -->
% include('_js_functions.tpl')

<!-- SCRIPTS END -->
<!-- ######################################################################################################### -->

</body>

</html>
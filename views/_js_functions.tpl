<script type="text/javascript">


function anchorToRequested () {
	var requested = document.getElementById("requested");
	var anchor = requested.attributes["data-anchor"].value;
	console.log("ANCHOR AT : " + anchor);
	window.location.hash = anchor;
}


</script>
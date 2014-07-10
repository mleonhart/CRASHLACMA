<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    <meta http-equiv="Refresh" content="30">

    <style type="text/css">
      html { height: 100% }
      body { height: 100%; margin: 0; padding: 0 }
      #map-canvas { height: 100% }
      .labels {
      	color: red;
      	background-color: white;
      	font-family: "Lucida Grande", "Arial", sans-serif;
     	font-size: 10px;
     	font-weight: bold;
     	text-align: center;
     	width: 40px;     
     	border: 2px solid black;
     	white-space: nowrap;
   }
    </style>
    
    <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?sensor=false"></script>

	<script type="text/javascript">
		var imgThumbStack = [];
	</script>

	<?php
		$dir    = '../data_finished_images';
		$files1 = scandir($dir, 1);

		// for each image file in the approved directory
		$count = 0;
		foreach ($files1 as $value) {
			if (strpos($value,'thumb') !== false && $count < 8) {		
	?>
	<script>
				imgThumbStack.push('<?php echo $value;?>');
				console.log(imgThumbStack);
				
				// just here for debug
				count = '<?php echo $count;?>';			
				console.log(count);
				// lock the files or rename them or something after
	</script>

	<?php
				//echo $dir . '/' . $value;
				//rename($dir . '/' . $value , $dir . '/DONE' . $value);
				$count++;		
			}
		}
	?>

    <script type="text/javascript">
      function initialize() {
        var mapOptions = {
          center: new google.maps.LatLng(34.0, -118.2),
          zoom: 11,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        
        var map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);
		
		// generates image thumbnails on the map
		for (var i = 0; i < imgThumbStack.length; i++) { 
			console.log("stack[" + i + "]: " + imgThumbStack[i]);

    		var marker = new google.maps.Marker({
    			position: new google.maps.LatLng(imgThumbStack[i].split("_")[2], imgThumbStack[i].split("_")[3]),
    			map: map,
    			labelContent: "0", 
    			icon: "../data_finished_images/" + imgThumbStack[i],
    			labelAnchor: new google.maps.Point(0, 50),
    			size: new google.maps.Size(50, 50),
    			labelClass: "labels", 
    			labelStyle: {opacity: 0.75},
    			title:"Nothing yet."
			});
		}
      }
      google.maps.event.addDomListener(window, 'load', initialize);
    </script>
  </head>
  <body>
    <div id="map-canvas"/>
  </body>
</html>

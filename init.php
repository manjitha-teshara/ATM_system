<?php 
    $db_name="androidDb";
    $mysql_user="root";
    $mysql_pass="";
    $server_name="localhost";

    $con=mysqli_connect($server_name,$mysql_user,$mysql_pass,$db_name);

    if(!$con){
        echo "connection Error...".mysqli_connect_error();
    }
else{
    echo "<h1>db connection success</h1>";
}
?>
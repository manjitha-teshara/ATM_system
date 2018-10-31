<?php 

            include("init.php");
            
            
            

            if(isset($_POST['submit'])){
                
                $userName = $_POST["userName"];
                $password = $_POST["password"];
                
                $sql_query="select userName from user where userName like '$userName' and password like '$password';";
                
                $result=mysqli_query($con,$sql_query);

                if(mysqli_num_rows($result)>0){
                    $row=mysqli_fetch_assoc($result);
                    $name=$row["userName"];
                    echo "Helo welcome ".$name;
                }

                else{
                    echo "No record in user...";
                }

            }
        
        

            
        ?>


<!DOCTYPE HTML>  
<html>
<head>
        <link rel="stylesheet" href="assets/css/login.css" />
        <script src="assets/js/login.js"></script>
</head>
    <body>
        
        <form method="post" id="loginFormId">
            <label>Email / Username</label><br/><br/>
		    <input type="text" name="userName" /><br/><br/>
			<br />

			<label>Password</label><br/><br/>
			<input type="password" name="password"/><br/><br/>
			<br />										

			<input type="submit" name="submit" value="Login"/> 
            
                    
        </form>
        
        
    </body>
</html>



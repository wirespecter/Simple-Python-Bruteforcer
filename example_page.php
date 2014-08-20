<html>
<head>
</head>
<body>
<form action='index.php' method='post'>
Username: <input type='text' name='user'>
Password: <input type='password' name='pass'>
<input type='submit' value='Login'>
</form>

<?php

$user=$_POST['user'];
$pass=$_POST['pass'];


if (($user=="admin") && ($pass=="php")) echo " Access Granted !";
else echo " Access Denied!";

?>
</body>
</html>

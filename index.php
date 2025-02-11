<?php
    
    if(isset($_POST['submit'])){
        
        $allowed_ext = array('pdf', 'doc', 'docx');

        if(!empty($_FILES['upload'])){
            $file_name = $_FILES['upload']['name'];
            $file_size = $_FILES['upload']['size'];
            $file_tmp_name = $_FILES['upload']['tmp_name'];
            $target_dir = "uploads/$file_name";

            // Get File extension
            $file_ext = explode('.', $file_name);
            $file_ext = strtolower(end($file_ext));

            // Validate file extension
            if(in_array($file_ext, $allowed_ext)){
                if($file_size <= 1000000000){
                    move_uploaded_file($file_tmp_name, $target_dir);
                    $msg = '<p style="color : green;">File uploaded successfully</p>';
                } else {
                    $msg = '<p style="color : red;">File size too large</p>';
                }
            } else {
                $msg = '<p style="color : red;">Invalid file type</p>';
            }
        } else {
            $msg = '<p style="color : red;">Please choose a file</p>';
        }
    }

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interview Assistant</title>
</head>
<body>
    <form action="<?php echo $_SERVER['PHP_SELF']; ?>" method="post" enctype="multipart/form-data">
        Upload Your Resume to upload:
        <input type="file" name="fileToUpload" id="fileToUpload">
        <input type="submit" value="Upload" name="submit">
    </form>
</body>
</html>
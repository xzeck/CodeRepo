print "Enter your number"

$number = <>; 

if($number == 2)
    print "It is a prime number";
else 
 {
     for($c = 2; $c<=$number/2; $c++)
     {
         if($number % $c == 0)
            $flag = 1;
            break;
     }
 }

 if($flag == 1)
    print "Not prime"
else 
    print "Prime"
$fact = 1;
$input = <>;


print $input;

if($input % 2 eq 0){
    $temp = $input;
    until($temp eq $zero )
    {
        $fact = $fact * $temp;
        $temp = $temp - 1
    }
}
else{
    print "Odd";
    for($c = 1; c<=$input; $c = $c+1)
    {
        $fact = $fact * $c
    }
}

print "The the factorial of $input is $fact"
$start = 0; 
$next = 1; 
$sum = 0;

$range = <>;

for($c = 0; $c<$range; $c++)
{
    print "\n$sum";
    $sum = $start + $next;
    $start = $next; 
    $next = $sum
}
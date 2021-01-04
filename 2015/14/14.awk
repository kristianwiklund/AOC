
{
    time = 2503
    interval = $7+$14
    maxints = int(time/interval)
    print(maxints*$4*$7+(time%interval>$7?$7*$4:(time%interval)*$4),$1 )
}

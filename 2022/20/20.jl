open("20.txt") do f
    N = parse.(Int, readlines(f))

    l = length(N)
    iN = collect(zip(1:l, N))
    for i ∈ 1:l
        j = findfirst(map(a->a[1]==i, iN))
        n = popat!(iN, j)
        insert!(iN, mod1(j+n[2],l-1), n)
    end
    zero = findfirst(map(a->a[2]==0, iN))
    println("Part 1: ", iN[mod1(zero+1000,l)][2]+iN[mod1(zero+2000,l)][2]+iN[mod1(zero+3000,l)][2])

    iN = collect(zip(1:l, N .* 811589153))
    for _ ∈ 1:10
        for i ∈ 1:l
            j = findfirst(map(a->a[1]==i, iN))
            n = popat!(iN, j)
            insert!(iN, mod1(j+n[2],l-1), n)
        end
    end
    zero = findfirst(map(a->a[2]==0, iN))
    println("Part 2: ", iN[mod1(zero+1000,l)][2]+iN[mod1(zero+2000,l)][2]+iN[mod1(zero+3000,l)][2])
end
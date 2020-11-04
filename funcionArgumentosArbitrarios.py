def concatenar(*args, sep="/"):
     return sep.join(args)

concatenar("tierra", "marte", "venus")
concatenar("tierra", "marte", "venus", sep=".")
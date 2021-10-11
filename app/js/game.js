// js function test
function makeSound (type = "dog") {
    const loweredType = type.toLowerCase();
    if ( loweredType === "dog") {
        return "Woof Woof!";
    } else if ( type === "cat") {
        return "Meoooooowwwww";
    } else if ( type === "horse" ) {
        return "Neeeiigghhh";
    }
}

export { makeSound };
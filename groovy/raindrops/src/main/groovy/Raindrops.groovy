class Raindrops {

    def convert(num) {
        String result = ""
        if(num % 3 == 0) {
            result += "Pling"
        }
        if(num % 5 == 0) {
            result += "Plang"
        }
        if(num % 7 == 0) {
            result += "Plong"
        }
        if ( result == "" ) {
            return num.toString()
        } else {
            return result
        }        
        throw new UnsupportedOperationException('Method implementation is missing')
    }

}

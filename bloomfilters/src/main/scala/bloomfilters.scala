package bloomfilters
object Hasher{
    private val md5 = java.security.MessageDigest.getInstance("MD5")
    def generate(word:String):String = {
        md5.reset();
        md5.update(word.getBytes("UTF-8"))
        val digested = md5.digest();
        val digestedArray = for (x <- digested) yield Integer.toHexString(0xff & x)    
        return digestedArray.mkString
    }
    def generateNumber(word:String, crop:Int):Int = {
        val hashed = generate(word)
        return ( hashed## ) % crop
    }

}

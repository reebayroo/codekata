import org.scalatest.WordSpec
import bloomfilters._


class HasherSpec  extends WordSpec {
    "Given a Hasher" when {
        "a generate is called" should {
            "return a value hashed when test is given" in {
                assert(Hasher.generate("test") == "98f6bcd4621d373cade4e832627b4f6")
            }
            "return a value hashed when zebra is given" in {
                assert(Hasher.generate("zebra") == "69c459dd76c6198f72f0c2ddd3c9447")
            }
        }
        "a generateNumber is called" should {
            "return a value 22  when test and 128 is given" in {
                assert(Hasher.generateNumber("test", 128) == 22)
            }
            "return a value 33942 when test and 64K is given" in {
                assert(Hasher.generateNumber("test", 64*1024) == 33942)
            }
        }
    }
}

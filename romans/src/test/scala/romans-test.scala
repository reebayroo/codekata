import org.scalatest._
import romans._;
class RomansSpec extends FlatSpec with Matchers {
      // Your tests here
      "A Roman Converter " should " change a range of simple tokens to roman chars " in {
         val converter = new Romans()
         converter.convert("I") should be (1)
         converter.convert("V") should be (5)
         converter.convert("X") should be (10)
         converter.convert("L") should be (50)

         converter.convert("C") should be (100)
         
         converter.convert("D") should be (500)
         converter.convert("M") should be (1000)
      }
      it should " add simple combinations " in {
         val converter = new Romans()
         converter.convert("II") should be (2)
         converter.convert("III") should be (3)
         //converter.convert("IV") should be (4)
         converter.convert("VI") should be (6)
         converter.convert("XIII") should be (13)
         converter.convert("LV") should be (55)

         converter.convert("CXX") should be (120)
         
         converter.convert("MD") should be (1500)
      }
          
      it should " add complex combinations " in {
         val converter = new Romans()
         converter.convert("IV") should be (4)
         converter.convert("VL") should be (45)
         converter.convert("CD") should be (400)
      }
}



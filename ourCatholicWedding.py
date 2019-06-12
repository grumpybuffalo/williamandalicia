# -*- coding: pyxl -*-
from pyxl import html

import page

def compile():
  mainContents = (
    <frag>
      <h2>
        OUR CATHOLIC WEDDING
      </h2>
      <article>
        <p>
          We’re excited about our upcoming Catholic wedding! We’d like our guests to understand what exactly we’re getting ourselves into. Here’s a quick overview of some of the special features of Catholic marriage.
        </p>
        <h3>
          <q>Marriage is not a purely human institution</q> <a href="http://www.vatican.va/archive/ccc_css/archive/catechism/p2s2c3a7.htm">(CCC 1603)</a>
        </h3>
        <p>
          As Catholics, we believe that <q>God Himself is the author of matrimony</q> <a href="http://www.vatican.va/archive/hist_councils/ii_vatican_council/documents/vat-ii_const_19651207_gaudium-et-spes_en.html">(Gaudium et spes)</a>. Marriage is a sacred bond, not just a legal contract. During His time on Earth, Jesus Christ upgraded marriage into a genuine sacrament. This means that marriage between two baptized Christians is an <q>efficacious sign of grace</q> by which <q>divine life is dispensed</q> to the spouses <a href="http://www.vatican.va/archive/ccc_css/archive/catechism/p2s1c1a2.htm">(CCC 1131)</a>.
        </p>
        <h3>
          <q>Till death do us part</q>
        </h3>
        <p>
          For Catholics, marriage is an extremely serious commitment. The Catholic Church teaches that a consummated, sacramental marriage only ends when one of the spouses dies. <q>The Church does not have the power</q> to end the marriage any earlier <a href="http://www.vatican.va/archive/ccc_css/archive/catechism/p2s2c3a7.htm">(CCC 1640)</a>. Even if spouses were to get a civil divorce, the sacred marriage bond would remain. As Jesus put it, <q>Whoever divorces his wife and marries another commits adultery against her; and if she divorces her husband and marries another, she commits adultery.</q> <a href="http://usccb.org/bible/mark/10">(Mark 10:11-12)</a>
        </p>
        <h3>
          <q>The two shall become one flesh</q>
        </h3>
        <p>
          The Catholic Church teaches that sex is <q>noble and honorable</q> <a href="http://www.vatican.va/archive/ccc_css/archive/catechism/p3s2c2a6.htm">(CCC 2362)</a>. However, all Catholics, married and unmarried, must practice the virtue of chastity. In this context, <dfn>chastity</dfn> means refusing to overindulge one’s appetite for sex. (Similarly, it’s good to refuse to overindulge one’s appetite for food!)
        </p>
        <p>
          The Catholic Church teaches that chastity comes in different forms. For unmarried people, chastity requires refraining from sex altogether. Within marriage, chaste sex is good and possible. Sex <q>achieves the twofold end of marriage: the good of the spouses themselves and the transmission of life</q> <a href="http://www.vatican.va/archive/ccc_css/archive/catechism/p3s2c2a6.htm">(CCC 2363)</a>. Spouses are right to seek out and enjoy the <q>pleasure and happiness of body and spirit</q> that come with sex <a href="https://www.ewtn.com/library/PAPALDOC/P511029.HTM">(Pope Pius XII, allocution to midwives, 10/29/1951)</a>.
        </p>
        <h3>
          What to expect at our wedding ceremony
        </h3>
        <p>
          Don’t worry if you’re not a practicing Catholic. Our wedding ceremony is open to people of any faith or no faith. Guests are not expected to do anything difficult. The role of guests at the ceremony is simply to supportively witness the wedding.
        </p>
        <p>
          Our wedding will take place during a Catholic Mass (as is traditional). In any Catholic Mass, there are several points where the congregation prays, sings, or says a creed together. Non-Catholic guests are welcome to participate or not participate at these times.
        </p>
        <p>
          Near the end of the Mass, the congregation comes forward to receive Jesus’ body and blood under the appearance of bread and wine (the Eucharist). If you’re not a practicing Catholic, please do not receive the Eucharist. We encourage you to come forward to receive a blessing; please cross your arms over your chest to indicate that you are not receiving the Eucharist. You’re also welcome to simply stay in your seat during this time.
        </p>
        <h3>
          How you can take part in our wedding right now
        </h3>
        <p>
          Please pray for us! We will be praying every Friday evening for our upcoming marriage. We would like to say prayers written by you, our friends and family. Please submit a prayer below so we can include it in our weekly prayers. Additionally, we invite you to pray your prayer every Friday evening too!
        </p>
      </article>
      <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeXTtqv65mwOCGikRzR64MRf5bo34k5bbSw1qo9kJ1lUwOIsg/viewform?embedded=true" height="691" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>
    </frag>
  )
  
  page.compile("our-catholic-wedding/index.html", mainContents, stylesheet="/our-catholic-wedding/index.css", title="Our Catholic Wedding")

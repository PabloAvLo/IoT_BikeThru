using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
//using System.Windows.Forms;
using System.Data.SqlClient;
//using System.Numerics;

namespace BT.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }

        public ActionResult About()
        {
            ViewBag.Message = "Your application description page.";

            return View();
        }

        public ActionResult Contact()
        {
            ViewBag.Message = "Your contact page.";

            return View();
        }

        public ActionResult Map()
        {
            return View();
        }

        public ActionResult Statistics()
        {
            //connecting to db / open connection
            SqlConnection con = new SqlConnection();
            con.ConnectionString = "data source = bikethru.database.windows.net; database = bikethru_db; user id = bikethru_root; password = Ingelectrica94";

            SqlCommand cmd = new SqlCommand("Select * from user_data", con);
            con.Open();
            SqlDataReader DR = cmd.ExecuteReader();

            //Creating lists for each column in DB
            List<string> myList1 = new List<string>();
            List<string> myList2 = new List<string>();
            List<string> myList3 = new List<string>();
            List<string> myList4 = new List<string>();
            List<Int16> myList5 = new List<Int16>();
            List<Int16> myList6 = new List<Int16>();
            List<int> myList7   = new List<int>();
            List<int> myList8   = new List<int>();
            List<int> myList9   = new List<int>();
            List<int> myList10  = new List<int>();         

            //Adding data to each list
            while (DR.Read())
            {
                var myString1   = DR.GetString(0);
                var myString2   = DR.GetString(1);
                var myString3   = DR.GetString(2);
                var myString4   = DR.GetString(3);
                var myInt5  = DR.GetInt16(4);
                var myInt6  = DR.GetInt16(5);
                var myInt7  = DR.GetInt32(6);
                var myInt8  = DR.GetInt32(7);
                var myInt9  = DR.GetInt32(8);
                var myInt10 = DR.GetInt32(9);

                //Adding data to lists
                myList1.Add(myString1);
                myList2.Add(myString2);
                myList3.Add(myString3);
                myList4.Add(myString4);
                myList5.Add(myInt5);
                myList6.Add(myInt6);
                myList7.Add(myInt7);
                myList8.Add(myInt8);
                myList9.Add(myInt9);
                myList10.Add(myInt10);
            }

            int list_size = myList1.Count;
            //Using viewbag to transfer data from homeController to view (statistics)
            ViewBag.Name        = myList1.GetRange(0, list_size);
            ViewBag.Carne       = myList2.GetRange(0, list_size);
            ViewBag.Email       = myList3.GetRange(0, list_size);
            ViewBag.Password    = myList4.GetRange(0, list_size);
            ViewBag.CI          = myList5.GetRange(0, list_size);
            ViewBag.CO          = myList6.GetRange(0, list_size);
            ViewBag.CIStation   = myList7.GetRange(0, list_size);
            ViewBag.COStation   = myList8.GetRange(0, list_size);
            ViewBag.RFID        = myList9.GetRange(0, list_size);
            ViewBag.barcode     = myList10.GetRange(0, list_size);

            //closing connection
            con.Close();
            return View();
        }
    }
}
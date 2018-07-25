from payload.rf_calc.receive_channel import ReceiveRFChannel


class TestCaseReceiveChannel:

    def test_down_convert_channel(self):
        ch_lo_bigger = ReceiveRFChannel(intermediate_frequency=5,
                                        local_oscillator_frequency=8,
                                        bandwidth_channel=1,
                                        converter_direction='down')
        assert ch_lo_bigger.main_receive()['center'] == 13
        assert ch_lo_bigger.image_receive()['center'] == 3
        assert ch_lo_bigger.intermediate_receive()['center'] == 5
        assert len(ch_lo_bigger.combinations_receive()) == 180
        assert len(ch_lo_bigger.subharmonic_receive()) == 30
        assert len(ch_lo_bigger.equal_nm_receive()) == 20

        ch_lo_less = ReceiveRFChannel(intermediate_frequency=5,
                                      local_oscillator_frequency=3,
                                      bandwidth_channel=2,
                                      converter_direction='down')
        assert ch_lo_less.main_receive()['center'] == 8
        assert ch_lo_less.image_receive()['center'] == 2

        ch = ReceiveRFChannel(intermediate_frequency=1,
                              local_oscillator_frequency=9,
                              bandwidth_channel=4,
                              converter_direction='down')
        print('\n', ch.image_receive(), '\n', ch.main_receive(), '\n', ch.intermediate_receive())

    def test_error_channel(self):
        ch = ReceiveRFChannel(intermediate_frequency=5,
                              local_oscillator_frequency=3,
                              bandwidth_channel=1,
                              converter_direction='next')
        try:
            ch.main_receive()
        except ValueError:
            pass
        try:
            ch.image_receive()
        except ValueError:
            pass

    def test_up_convert_channel(self):
        ch = ReceiveRFChannel(intermediate_frequency=10,
                              local_oscillator_frequency=3,
                              bandwidth_channel=1,
                              converter_direction='up')

        assert ch.image_receive()['center'] == 13
        assert ch.main_receive()['center'] == 7

    def test_inverse_channel(self):
        ch = ReceiveRFChannel(intermediate_frequency=6,
                              local_oscillator_frequency=8,
                              bandwidth_channel=1,
                              converter_direction='inverse')

        assert ch.main_receive()['center'] == 2
        assert ch.image_receive()['center'] == 14
